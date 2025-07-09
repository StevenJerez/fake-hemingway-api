# analyzer.py

import re
from typing import List, Dict, Tuple

def get_ly_words() -> set:
    """
    Return a set of common '-ly' words that should NOT be counted as adverbs.
    """
    return {
        "actually", "additionally", "allegedly", "ally", "alternatively", "anomaly",
        "apply", "approximately", "ashely", "ashly", "assembly", "awfully", "baily",
        "belly", "bely", "billy", "bradly", "bristly", "bubbly", "bully", "burly",
        "butterfly", "carly", "charly", "chilly", "comely", "completely", "comply",
        "consequently", "costly", "courtly", "crinkly", "crumbly", "cuddly",
        "curly", "currently", "daily", "dastardly", "deadly", "deathly", "definitely",
        "dilly", "disorderly", "doily", "dolly", "dragonfly", "early", "elderly",
        "elly", "emily", "especially", "exactly", "exclusively", "family", "finally",
        "firefly", "folly", "friendly", "frilly", "gadfly", "gangly", "generally",
        "ghastly", "giggly", "globally", "goodly", "gravelly", "grisly", "gully",
        "haily", "hally", "harly", "hardly", "heavenly", "hillbilly", "hilly",
        "holly", "holy", "homely", "homily", "horsefly", "hourly", "immediately",
        "instinctively", "imply", "italy", "jelly", "jiggly", "jilly", "jolly", "july",
        "karly", "kelly", "kindly", "lately", "likely", "lilly", "lily", "lively",
        "lolly", "lonely", "lovely", "lowly", "luckily", "mealy", "measly", "melancholy",
        "mentally", "molly", "monopoly", "monthly", "multiply", "nightly", "oily", "only",
        "orderly", "panoply", "particularly", "partly", "paully", "pearly", "pebbly",
        "polly", "potbelly", "presumably", "previously", "pualy", "quarterly", "rally",
        "rarely", "recently", "rely", "reply", "reportedly", "roughly", "sally", "scaly",
        "shapely", "shelly", "shirly", "shortly", "sickly", "silly", "sly", "smelly",
        "sparkly", "spindly", "spritely", "squiggly", "stately", "steely", "supply",
        "surly", "tally", "timely", "trolly", "ugly", "underbelly", "unfortunately",
        "unholy", "unlikely", "usually", "waverly", "weekly", "wholly", "willy", "wily",
        "wobbly", "wooly", "worldly", "wrinkly", "yearly"
    }

def get_complex_words() -> Dict[str, List[str]]:
    """
    Return a mapping of complex phrases to simpler replacements.
    """
    return {
        "a number of": ["many", "some"],
        "abundance": ["enough", "plenty"],
        "accede to": ["allow", "agree to"],
        "accelerate": ["speed up"],
        "accentuate": ["stress"],
        "accompany": ["go with", "with"],
        "accomplish": ["do"],
        "accorded": ["given"],
        "accrue": ["add", "gain"],
        "acquiesce": ["agree"],
        "acquire": ["get"],
        "additional": ["more", "extra"],
        "adjacent to": ["next to"],
        "adjustment": ["change"],
        "admissible": ["allowed", "accepted"],
        "advantageous": ["helpful"],
        "adversely impact": ["hurt"],
        "advise": ["tell"],
        "aforementioned": ["remove"],
        "aggregate": ["total", "add"],
        "aircraft": ["plane"],
        "all of": ["all"],
        "alleviate": ["ease", "reduce"],
        "allocate": ["divide"],
        "along the lines of": ["like", "as in"],
        "already existing": ["existing"],
        "alternatively": ["or"],
        "ameliorate": ["improve", "help"],
        "anticipate": ["expect"],
        "apparent": ["clear", "plain"],
        "appreciable": ["many"],
        "as a means of": ["to"],
        "as of yet": ["yet"],
        "as to": ["on", "about"],
        "as yet": ["yet"],
        "ascertain": ["find out", "learn"],
        "assistance": ["help"],
        "at this time": ["now"],
        "attain": ["meet"],
        "attributable to": ["because"],
        "authorize": ["allow", "let"],
        "because of the fact that": ["because"],
        "belated": ["late"],
        "benefit from": ["enjoy"],
        "bestow": ["give", "award"],
        "by virtue of": ["by", "under"],
        "cease": ["stop"],
        "close proximity": ["near"],
        "commence": ["begin", "start"],
        "comply with": ["follow"],
        "concerning": ["about", "on"],
        "consequently": ["so"],
        "consolidate": ["join", "merge"],
        "constitutes": ["is", "forms", "makes up"],
        "demonstrate": ["prove", "show"],
        "depart": ["leave", "go"],
        "designate": ["choose", "name"],
        "discontinue": ["drop", "stop"],
        "due to the fact that": ["because", "since"],
        "each and every": ["each"],
        "economical": ["cheap"],
        "eliminate": ["cut", "drop", "end"],
        "elucidate": ["explain"],
        "employ": ["use"],
        "endeavor": ["try"],
        "enumerate": ["count"],
        "equitable": ["fair"],
        "equivalent": ["equal"],
        "evaluate": ["test", "check"],
        "evidenced": ["showed"],
        "exclusively": ["only"],
        "expedite": ["hurry"],
        "expend": ["spend"],
        "expiration": ["end"],
        "facilitate": ["ease", "help"],
        "factual evidence": ["facts", "evidence"],
        "feasible": ["workable"],
        "finalize": ["complete", "finish"],
        "first and foremost": ["first"],
        "for the purpose of": ["to"],
        "forfeit": ["lose", "give up"],
        "formulate": ["plan"],
        "honest truth": ["truth"],
        "however": ["but", "yet"],
        "if and when": ["if", "when"],
        "impacted": ["affected", "harmed", "changed"],
        "implement": ["install", "put in place", "tool"],
        "in a timely manner": ["on time"],
        "in accordance with": ["by", "under"],
        "in addition": ["also", "besides", "too"],
        "in all likelihood": ["probably"],
        "in an effort to": ["to"],
        "in between": ["between"],
        "in excess of": ["more than"],
        "in lieu of": ["instead"],
        "in light of the fact that": ["because"],
        "in many cases": ["often"],
        "in order to": ["to"],
        "in regard to": ["about", "concerning", "on"],
        "in some instances": ["sometimes"],
        "in terms of": ["omit"],
        "in the near future": ["soon"],
        "in the process of": ["omit"],
        "inception": ["start"],
        "incumbent upon": ["must"],
        "indicate": ["say", "state", "or show"],
        "indication": ["sign"],
        "initiate": ["start"],
        "is applicable to": ["applies to"],
        "is authorized to": ["may"],
        "is responsible for": ["handles"],
        "it is essential": ["must", "need to"],
        "literally": ["omit"],
        "magnitude": ["size"],
        "maximum": ["greatest", "largest", "most"],
        "methodology": ["method"],
        "minimize": ["cut"],
        "minimum": ["least", "smallest", "small"],
        "modify": ["change"],
        "monitor": ["check", "watch", "track"],
        "multiple": ["many"],
        "necessitate": ["cause", "need"],
        "nevertheless": ["still", "besides", "even so"],
        "not certain": ["uncertain"],
        "not many": ["few"],
        "not often": ["rarely"],
        "not unless": ["only if"],
        "not unlike": ["similar", "alike"],
        "notwithstanding": ["in spite of", "still"],
        "null and void": ["use either null or void"],
        "numerous": ["many"],
        "objective": ["aim", "goal"],
        "obligate": ["bind", "compel"],
        "obtain": ["get"],
        "on the contrary": ["but", "so"],
        "on the other hand": ["but", "so"],
        "one particular": ["one"],
        "optimum": ["best", "greatest", "most"],
        "overall": ["omit"],
        "owing to the fact that": ["because", "since"],
        "participate": ["take part"],
        "particulars": ["details"],
        "pass away": ["die"],
        "pertaining to": ["about", "of", "on"],
        "point in time": ["time", "point", "moment", "now"],
        "portion": ["part"],
        "possess": ["have", "own"],
        "preclude": ["prevent"],
        "previously": ["before"],
        "prior to": ["before"],
        "prioritize": ["rank", "focus on"],
        "procure": ["buy", "get"],
        "proficiency": ["skill"],
        "provided that": ["if"],
        "purchase": ["buy", "sale"],
        "put simply": ["omit"],
        "readily apparent": ["clear"],
        "refer back": ["refer"],
        "regarding": ["about", "of", "on"],
        "relocate": ["move"],
        "remainder": ["rest"],
        "remuneration": ["payment"],
        "require": ["must", "need"],
        "requirement": ["need", "rule"],
        "reside": ["live"],
        "residence": ["house"],
        "retain": ["keep"],
        "satisfy": ["meet", "please"],
        "shall": ["must", "will"],
        "should you wish": ["if you want"],
        "similar to": ["like"],
        "solicit": ["ask for", "request"],
        "span across": ["span", "cross"],
        "strategize": ["plan"],
        "subsequent": ["later", "next", "after", "then"],
        "substantial": ["large", "much"],
        "successfully complete": ["complete", "pass"],
        "sufficient": ["enough"],
        "terminate": ["end", "stop"],
        "the month of": ["omit"],
        "therefore": ["thus", "so"],
        "this day and age": ["today"],
        "time period": ["time", "period"],
        "took advantage of": ["preyed on"],
        "transmit": ["send"],
        "transpire": ["happen"],
        "until such time as": ["until"],
        "utilization": ["use"],
        "utilize": ["use"],
        "validate": ["confirm"],
        "various different": ["various", "different"],
        "whether or not": ["whether"],
        "with respect to": ["on", "about"],
        "with the exception of": ["except for"],
        "witnessed": ["saw", "seen"]
    }

def get_qualifying_words() -> set:
    """
    Return a set of qualifier phrases that weaken statements.
    """
    return {
        "i believe", "i consider", "i don't believe", "i don't consider",
        "i don't feel", "i don't suggest", "i don't think", "i feel",
        "i hope to", "i might", "i suggest", "i think", "i was wondering",
        "i will try", "i wonder", "in my opinion", "is kind of",
        "is sort of", "just", "maybe", "perhaps", "possibly",
        "we believe", "we consider", "we don't believe", "we don't consider",
        "we don't feel", "we don't suggest", "we don't think", "we feel",
        "we hope to", "we might", "we suggest", "we think",
        "we were wondering", "we will try", "we wonder"
    }

def split_sentences(text: str) -> List[str]:
    """
    Split text into sentences based on punctuation.
    """
    parts = re.split(r'(?<=[.!?]) +', text.strip())
    return [p for p in parts if p]

def analyze_text(text: str) -> Tuple[dict, List[dict]]:
    """
    Analyze the text and return metrics and list of suggestions.
    """
    data = {
        "paragraphs": text.count("\n") + 1,
        "sentences": 0,
        "words": 0,
        "letters": 0,
        "adverbs": 0,
        "passive": 0,
        "complex": 0,
        "qualifiers": 0
    }
    suggestions: List[dict] = []

    ly_whitelist = get_ly_words()
    complex_map = get_complex_words()
    qualifier_set = get_qualifying_words()

    for paragraph in text.split("\n"):
        sentences = split_sentences(paragraph)
        data["sentences"] += len(sentences)

        for sent in sentences:
            clean = re.sub(r'[^A-Za-z0-9 ]', "", sent)
            words = clean.split()
            data["words"] += len(words)
            data["letters"] += sum(len(w) for w in words)

            # detect adverbs
            for w in words:
                if w.lower().endswith("ly") and w.lower() not in ly_whitelist:
                    data["adverbs"] += 1
                    suggestions.append({
                        "offset": None,
                        "length": len(w),
                        "type": "adverb",
                        "suggestion": f"Avoid the adverb '{w}'"
                    })

            # detect passive voice
            tokens = sent.split()
            for i, token in enumerate(tokens):
                if re.match(r".+ed[.,]?$", token.lower()):
                    prev = tokens[i-1].lower() if i > 0 else ""
                    if prev in {"is","are","was","were","be","been","being"}:
                        data["passive"] += 1
                        suggestions.append({
                            "offset": None,
                            "length": len(tokens[i-1]) + len(token) + 1,
                            "type": "passive",
                            "suggestion": "Rephrase to active voice"
                        })

            # detect complex phrases
            lower_sent = sent.lower()
            for phrase, repls in complex_map.items():
                if phrase in lower_sent:
                    data["complex"] += 1
                    suggestions.append({
                        "offset": None,
                        "length": len(phrase),
                        "type": "complex",
                        "suggestion": f"Replace '{phrase}' with '{repls[0]}'"
                    })

            # detect qualifiers
            for qualifier in qualifier_set:
                if qualifier in lower_sent:
                    data["qualifiers"] += 1
                    suggestions.append({
                        "offset": None,
                        "length": len(qualifier),
                        "type": "qualifier",
                        "suggestion": f"Consider removing qualifier '{qualifier}'"
                    })

    data["readability_score"] = round(
        206.835 - 1.015 * (data["words"] / data["sentences"] if data["sentences"] else 0)
        - 84.6 * (data["letters"] / data["words"] if data["words"] else 0),
        2
    )

    return data, suggestions

def rewrite_text(text: str) -> str:
    """
    Rewrite text by applying first-pass simplifications.
    """
    _, suggestions = analyze_text(text)
    output = text

    for s in suggestions:
        # extract target and replacement
        match = re.search(r"'(.+?)'", s["suggestion"])
        if not match:
            continue
        target = re.escape(match.group(1))
        if s["type"] == "complex":
            replacement = s["suggestion"].split("with '")[-1].rstrip("'")
        else:
            replacement = ""
        output = re.sub(target, replacement, output, count=1)

    return output