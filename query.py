def select_files(program, language):
    """
    Selects all the .naf files from the specified program(s) and language(s).

    Args:
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      A list of thesis files in the specified program(s) and language(s).
    """
    import os
    # Error handling
    if type(program) != list:
        raise TypeError('The argument program has to be the type "list", e.g., \
        ["arch", "tlw"]')
    if type(language) != list:
        raise TypeError('The argument language has to be the type "list", e.g.,\
         ["en"]')

    for prog in program:
        if prog not in ["arch", "ciw", "erf", "esmus", "fil", "ges", "kcw",
                        "ltk", "ohs", "ph", "rgs", "rkcw", "rltk", "rohs",
                        "rtlw", "tlw"]:
            raise Exception("The specified program(s) not in the list. Please \
            check the spelling and the input format.")
    for lang in language:
        if lang not in ["en", "nl"]:
            raise Exception('The specified language(s) not permitted. Only \
            English ("en") and Dutch ("nl") allowed. Please check the spelling \
            and the input format.')

    list_file = []
    # Uses multiple loops to find all the files
    for prog in program:
        for lang in language:
            directory = os.path.join("thesis_vu_2015", prog, lang)
            for root, dirs, files in os.walk(directory):
                for filename in files:

                    # Only the files with .nohyphen are wanted
                    if filename.endswith("nohyphen"):
                        filepath = os.path.join(root, filename)
                        list_file.append(filepath)
    return list_file


def generate_tokens(filename):
    """
    Generates tokens/words in the element "wf".

    Arg:
      filename: The path to the file to be processed. @type: string

    Returns:
      A generator that yields tokens/words in the given file.
    """
    from lxml import etree
    xml = etree.parse(filename)
    root = xml.getroot()

    # Creates a list of all the wf elements
    list_wf_el = root.xpath("/NAF/text/wf")
    for wf_el in list_wf_el:
        token = wf_el.text

        # Checks if the token is a word
        if is_word(token):
            yield token


def generate_types(filename):
    """
    Generates types/lemmas in the attribute "lemma" of the element "term".

    Arg:
      filename: The path to the file to be processed. @type: string

    Returns:
      A generator that yields types/lemmas in the given file.
    """
    from lxml import etree
    xml = etree.parse(filename)
    root = xml.getroot()
    list_term = root.xpath("/NAF/terms/term")
    for term in list_term:
        lemma = term.get("lemma")

        # Checks if the lemma is a word
        if is_word(lemma):
            yield lemma


def is_word(word_form):
    """
    Checks if the input word_form is a word.

    Arg:
      word_form: The word form to be checked. @type: string

    Returns:
      A boolean expression indicating if the input is a word.
    """
    import string
    nonalphabetic = string.punctuation + string.digits # Characters not wanted
    for char in word_form:
        if char not in nonalphabetic:
            return True
    return False


def generate_sent_id(filename):
    """
    Generates sentence id's in the attribute "sent" of the element "wf".

    Arg:
      filename: The path to the file to be processed. @type: string

    Returns:
      A generator that yields sentence id's in the given file.
    """
    from lxml import etree
    xml = etree.parse(filename)
    root = xml.getroot()
    list_wf_el = root.xpath("/NAF/text/wf")
    for wf_el in list_wf_el:
        wf = wf_el.text
        if is_word(wf):
            sent_id = wf_el.get("sent")
            yield sent_id


def dict_sent(program, language):
    """
    Creates a dictionary that maps a filename to a counter dictionary that maps
    sentence id's to the number of words in the sentence.
    e.g. {"filename": {"300": 107, "365": 106, "1117": 93, "223": 92}}

    Args:
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      A dictionary object.
    """
    from collections import Counter
    list_thesis = select_files(program, language)
    dict_sentences = dict()
    for thesis in list_thesis:
        # Creates a counter dictionary that maps sentence id to the number of
        # words that sentence contains.
        dict_len = Counter()
        generator_sent_id = generate_sent_id(thesis)
        for sent_id in generator_sent_id:
            dict_len[sent_id] += 1
        dict_sentences[thesis] = dict_len
    return dict_sentences


def dict_freq(kind, program, language):
    """
    Creates a counter dictionary that maps types or tokens to their
    frequency.

    Args:
      kind: token or type. @type: The string "token" or "type"
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      A counter dictionary.
    """
    from collections import Counter

    # Error handling
    if kind not in ["token", "type"]:
        raise Exception('The kind argument can only be either the string \
        "token" or "type".')

    try:
        list_thesis = select_files(program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    dict_frequency = Counter()
    for thesis in list_thesis:

        # Decides the kind
        if kind == "token":
            generator = generate_tokens(thesis)
        else:
            generator = generate_types(thesis)

        for item in generator:
            dict_frequency[item] += 1
    return dict_frequency


def average_number(kind, program, language):
    """
    Calculates and prints the average number of types or tokens of the theses \
    in the specified program(s) and language(s).

    Args:
      kind: token or type. @type: The string "token" or "type"
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      None.
    """
    # Error handling
    try:
        list_thesis = select_files(program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    try:
        dict_frequency = dict_freq(kind, program, language)
    except Exception as e:
        print(e)
        return

    number_thesis = len(list_thesis)
    if kind == "token":
        number_item = sum(dict_frequency.values())
    else:
        number_item = len(dict_frequency)
    avg_number_item = number_item / number_thesis
    print(avg_number_item)


def average_number_sent(program, language):
    """
    Calculates and prints the average number of sentences of the theses in the
    specified program(s) and language(s).

    Args:
      kind: token or type. @type: The string "token" or "type"
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      None.
    """
    # Error handling
    try:
        dict_sentence = dict_sent(program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    number_thesis = len(dict_sentence)
    list_dict_sent = dict_sentence.values()

    total_number_sent = 0
    for dic in list_dict_sent:
        number_sent = len(dic)
        total_number_sent += number_sent
    avg_number_sent = total_number_sent / number_thesis
    print(avg_number_sent)


def type_token_ratio(program, language):
    """
    Calculates and prints the type token ratio of words in the theses in the
    specified program(s) and language(s).

    Args:
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      None.
    """
    # Error handling
    try:
        dict_type = dict_freq("type", program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    number_type = len(dict_type)

    dict_token = dict_freq("token", program, language)
    number_token = sum(dict_token.values())
    ttr = number_type / number_token
    print(ttr)


def longest_sent(rank, program, language):
    """
    Prints the first n (i.e., rank) longest sentences in the theses in the
    specified program(s) and language(s).

    Args:
      rank: the number of the long sentences. @rank: integer
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      None.
    """
    from lxml import etree
    # Error handling
    try:
        dict_sentence = dict_sent(program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    if type(rank) != int:
        print("The argument rank can only be an integer.")
        return

    # Creates a dictionary that maps that length of a sentence to a list of
    # tuples in which the first element is the source file and the second is
    # the sentence id.
    # e.g., {20: [(filename_1, "123"), (filename_2, "23")]}
    dict_length = dict()

    for filename, counter in dict_sentence.items():
        for sent_id, length in counter.items():
            if dict_length.get(length, False):
                dict_length[length].append((filename, sent_id))
            else:
                dict_length[length] = [(filename, sent_id)]

    list_length_key = list(dict_length.keys())
    list_length_key.sort(reverse=True)

    rank_cnt = 0
    for length in list_length_key:
        if rank_cnt < rank:
            rank_cnt += len(dict_length[length])
            for filename, sent_id in dict_length[length]:
                xml = etree.parse(filename)
                root = xml.getroot()
                list_wf_el = root.xpath('/NAF/text/wf[@sent="%s"]' % sent_id)
                sent = ""
                for wf_el in list_wf_el:
                    word = wf_el.text
                    sent = sent + word + " "
                print("Rank ", rank_cnt, ", ", length," words, from ", filename,
                ":", sep="")
                print(sent, end="\n\n")


def dict_id_lemma(filename):
    """
    Creates a dictionary mapping word_id to its lemma in a given file.

    Arg:
      filename: The path to the file to be processed. @type: string

    Returns:
      A dictionary object.
    """
    from lxml import etree
    xml = etree.parse(filename)
    root = xml.getroot()
    list_term = root.xpath("/NAF/terms/term")
    dict_id_to_lemma = dict()
    for term in list_term:
        lemma_id = term.get("id")
        lemma = term.get("lemma")
        dict_id_to_lemma[lemma_id] = lemma
    return dict_id_to_lemma


def dict_entity_freq(program, language):
    """
    Creates a counter dictionary that maps enitities to their
    frequency in the theses in the specified program(s) and language(s).

    Args:
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      A counter dictionary.
    """
    from collections import Counter
    from lxml import etree

    # Error handling
    try:
        list_thesis = select_files(program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    cnt_entity_freq = Counter()
    for thesis in list_thesis:
        dict_id_to_lemma = dict_id_lemma(thesis)

        xml = etree.parse(thesis)
        root = xml.getroot()
        list_span = root.xpath("/NAF/entities/entity/references/span")
        for span in list_span:
            list_target = span.xpath("./target")
            list_targetwords = []
            for target in list_target:
                target_id = target.get("id")
                target_lemma = dict_id_to_lemma[target_id]
                list_targetwords.append(target_lemma)
            targetword = " ".join(list_targetwords)
            cnt_entity_freq[targetword] += 1
    return cnt_entity_freq


def most_common_entity(tp, rank, program, language):
    """
    Prints the first n most common entity of a certain type in the specified
    program(s) and language(s).

    Args:
      tp: the type of entity, either "person" or "place". @type: string "person"
          or "place"
      rank: the number of the long sentences. @type: integer
      program: program(s) to which theses belong. @type: list of strings
      language: language(s) of theses. @type: list of strings

    Returns:
      None.
    """
    from collections import Counter
    from lxml import etree

    # Error handling
    if not (tp == "person" or tp == "place"):
        print('The argument tp can only be either the string "person" or \
        "place".')
        return

    if type(rank) != int:
        print("The argument rank can only be an integer.")
        return

    try:
        list_thesis = select_files(program, language)
    except TypeError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    cnt_type_entity = Counter()
    for thesis in list_thesis:
        dict_id_to_lemma = dict_id_lemma(thesis)
        xml = etree.parse(thesis)
        root = xml.getroot()
        list_entity = root.xpath("/NAF/entities/entity")
        for entity in list_entity:
            if tp == "person":
                keyword = "DBpedia:Person"
            else:
                keyword = "DBpedia:Place"
            typ = entity.get("type")
            if keyword in typ:
                list_target = entity.xpath("./references/span/target")
                list_targetwords = []
                for target in list_target:
                    targetword_id = target.get("id")
                    targetword_lemma = dict_id_to_lemma[targetword_id]
                    list_targetwords.append(targetword_lemma)
                targetword = " ".join(list_targetwords)
                cnt_type_entity[targetword] += 1

    list_common_word = cnt_type_entity.most_common(rank)
    print("Rank", "Entity", "Frequency", sep="\t")
    for order, common_word in enumerate(list_common_word):
        print(order+1, common_word[0], common_word[1], sep="\t")
