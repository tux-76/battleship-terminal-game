from player import Player


# CONSTANTS
# ======================================================================
AI_PRESETS = ( # placement, finding, destroying
    (None, None, None), # custom preset
    (0, 0, 0),
    (0, 0, 2)
)

# FORMAT = (CONTENT, DIFFICULTY)
# DIFFICULTIES: 0:none, 1:super easy, 2:easy, 3:normal, 4:hard, 5:super hard, 6:impossibly hard
AI_PRESET_NAMES = (
    ("Custom", 0),
    ("Complete Random", 1),
    ("Random", 3),
)
# Custom modes
AI_PLACEMENT_MODE_NAMES = (
    ("Random", 3),
)
AI_LOCATION_MODE_NAMES = (
    ("Random", 3),
)
AI_DESTROYING_MODE_NAMES = (
    ("None", 1),
    ("Random Adjacent", 2),
    ("Random Directional (best)", 4)
)


# CLASS
# ===================================================================
class AI(Player):
    def __init__(self, screen, methodIDTuple) -> None:
        # create method tuple code to identify ai
        methodTupleCode = ""
        for methodID in methodIDTuple:
            methodTupleCode = methodTupleCode + str(methodID) + ";"
        methodTupleCode = methodTupleCode.removesuffix(";")
        self.methodTupleCode = methodTupleCode

        # get display name of ai
        if methodIDTuple in AI_PRESETS:
            nameEntry = AI_PRESET_NAMES[AI_PRESETS.index(methodIDTuple)]
            name = nameEntry[0]
            self.difficulty = nameEntry[1]
        else:
            name = "CUSTOM(" + methodTupleCode + ")"
        super().__init__(screen, name, "AI")