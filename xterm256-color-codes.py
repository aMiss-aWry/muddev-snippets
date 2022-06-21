import math

xterm_color_data = [{"colorId": "000", "hexString": "#000000", "rgb": {"r": 0, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 0, "l": 0}, "name": "Too Black"},
                    {"colorId": "R", "hexString": "#800000", "rgb": {"r": 128, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 25}, "name": "Maroon"},
                    {"colorId": "G", "hexString": "#008000", "rgb": {"r": 0, "g": 128, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 25}, "name": "Green"},
                    {"colorId": "Y", "hexString": "#808000", "rgb": {"r": 128, "g": 128, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 25}, "name": "Olive"},
                    {"colorId": "B", "hexString": "#000080", "rgb": {"r": 0, "g": 0, "b": 128}, "hsl": {"h": 240, "s": 100, "l": 25}, "name": "Dark blue"},
                    {"colorId": "M", "hexString": "#800080", "rgb": {"r": 128, "g": 0, "b": 128}, "hsl": {"h": 300, "s": 100, "l": 25}, "name": "Purple"},
                    {"colorId": "C", "hexString": "#008080", "rgb": {"r": 0, "g": 128, "b": 128}, "hsl": {"h": 180, "s": 100, "l": 25}, "name": "Teal"},
                    {"colorId": "w", "hexString": "#c0c0c0", "rgb": {"r": 192, "g": 192, "b": 192}, "hsl": {"h": 0, "s": 0, "l": 75}, "name": "Silver"},
                    {"colorId": "x", "hexString": "#808080", "rgb": {"r": 128, "g": 128, "b": 128}, "hsl": {"h": 0, "s": 0, "l": 50}, "name": "Grey"},
                    {"colorId": "r", "hexString": "#ff0000", "rgb": {"r": 255, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 50}, "name": "Red"},
                    {"colorId": "g", "hexString": "#00ff00", "rgb": {"r": 0, "g": 255, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 50}, "name": "Lime"},
                    {"colorId": "y", "hexString": "#ffff00", "rgb": {"r": 255, "g": 255, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 50}, "name": "Yellow"},
                    {"colorId": "b", "hexString": "#0000ff", "rgb": {"r": 0, "g": 0, "b": 255}, "hsl": {"h": 240, "s": 100, "l": 50}, "name": "Blue"},
                    {"colorId": "m", "hexString": "#ff00ff", "rgb": {"r": 255, "g": 0, "b": 255}, "hsl": {"h": 300, "s": 100, "l": 50}, "name": "Fuchsia"},
                    {"colorId": "c", "hexString": "#00ffff", "rgb": {"r": 0, "g": 255, "b": 255}, "hsl": {"h": 180, "s": 100, "l": 50}, "name": "Aqua"},
                    {"colorId": "w", "hexString": "#ffffff", "rgb": {"r": 255, "g": 255, "b": 255}, "hsl": {"h": 0, "s": 0, "l": 100}, "name": "White"},
                    {"colorId": "000", "hexString": "#000000", "rgb": {"r": 0, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 0, "l": 0}, "name": "Too Black"},
                    {"colorId": "001", "hexString": "#00005f", "rgb": {"r": 0, "g": 0, "b": 95}, "hsl": {"h": 240, "s": 100, "l": 18}, "name": "Midnight blue"},
                    {"colorId": "002", "hexString": "#000087", "rgb": {"r": 0, "g": 0, "b": 135}, "hsl": {"h": 240, "s": 100, "l": 26}, "name": "Indigo"},
                    {"colorId": "003", "hexString": "#0000af", "rgb": {"r": 0, "g": 0, "b": 175}, "hsl": {"h": 240, "s": 100, "l": 34}, "name": "Lapis lazuli"},
                    {"colorId": "004", "hexString": "#0000d7", "rgb": {"r": 0, "g": 0, "b": 215}, "hsl": {"h": 240, "s": 100, "l": 42}, "name": "Royal blue"},
                    {"colorId": "005", "hexString": "#0000ff", "rgb": {"r": 0, "g": 0, "b": 255}, "hsl": {"h": 240, "s": 100, "l": 50}, "name": "Blue"},
                    {"colorId": "010", "hexString": "#005f00", "rgb": {"r": 0, "g": 95, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 18}, "name": "Forest green"},
                    {"colorId": "011", "hexString": "#005f5f", "rgb": {"r": 0, "g": 95, "b": 95}, "hsl": {"h": 180, "s": 100, "l": 18}, "name": "Viridian"},
                    {"colorId": "012", "hexString": "#005f87", "rgb": {"r": 0, "g": 95, "b": 135}, "hsl": {"h": 197.777777777778, "s": 100, "l": 26}, "name": "Deep teal"},
                    {"colorId": "013", "hexString": "#005faf", "rgb": {"r": 0, "g": 95, "b": 175}, "hsl": {"h": 207.428571428571, "s": 100, "l": 34}, "name": "Daybreak blue"},
                    {"colorId": "014", "hexString": "#005fd7", "rgb": {"r": 0, "g": 95, "b": 215}, "hsl": {"h": 213.488372093023, "s": 100, "l": 42}, "name": "Sapphire"},
                    {"colorId": "015", "hexString": "#005fff", "rgb": {"r": 0, "g": 95, "b": 255}, "hsl": {"h": 217.647058823529, "s": 100, "l": 50}, "name": "Cobalt"},
                    {"colorId": "020", "hexString": "#008700", "rgb": {"r": 0, "g": 135, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 26}, "name": "Green"},
                    {"colorId": "021", "hexString": "#00875f", "rgb": {"r": 0, "g": 135, "b": 95}, "hsl": {"h": 162.222222222222, "s": 100, "l": 26}, "name": "Jungle green"},
                    {"colorId": "022", "hexString": "#008787", "rgb": {"r": 0, "g": 135, "b": 135}, "hsl": {"h": 180, "s": 100, "l": 26}, "name": "Teal"},
                    {"colorId": "023", "hexString": "#0087af", "rgb": {"r": 0, "g": 135, "b": 175}, "hsl": {"h": 193.714285714286, "s": 100, "l": 34}, "name": "Riverbed blue"},
                    {"colorId": "024", "hexString": "#0087d7", "rgb": {"r": 0, "g": 135, "b": 215}, "hsl": {"h": 202.325581395349, "s": 100, "l": 42}, "name": "Ocean blue"},
                    {"colorId": "025", "hexString": "#0087ff", "rgb": {"r": 0, "g": 135, "b": 255}, "hsl": {"h": 208.235294117647, "s": 100, "l": 50}, "name": "Azure"},
                    {"colorId": "030", "hexString": "#00af00", "rgb": {"r": 0, "g": 175, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 34}, "name": "Lawn green"},
                    {"colorId": "031", "hexString": "#00af5f", "rgb": {"r": 0, "g": 175, "b": 95}, "hsl": {"h": 152.571428571429, "s": 100, "l": 34}, "name": "Malachite"},
                    {"colorId": "032", "hexString": "#00af87", "rgb": {"r": 0, "g": 175, "b": 135}, "hsl": {"h": 166.285714285714, "s": 100, "l": 34}, "name": "Jade"},
                    {"colorId": "033", "hexString": "#00afaf", "rgb": {"r": 0, "g": 175, "b": 175}, "hsl": {"h": 180, "s": 100, "l": 34}, "name": "Blue-green"},
                    {"colorId": "034", "hexString": "#00afd7", "rgb": {"r": 0, "g": 175, "b": 215}, "hsl": {"h": 191.162790697674, "s": 100, "l": 42}, "name": "Turquoise"},
                    {"colorId": "035", "hexString": "#00afff", "rgb": {"r": 0, "g": 175, "b": 255}, "hsl": {"h": 198.823529411765, "s": 100, "l": 50}, "name": "Cerulean"},
                    {"colorId": "040", "hexString": "#00d700", "rgb": {"r": 0, "g": 215, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 42}, "name": "Grass green"},
                    {"colorId": "041", "hexString": "#00d75f", "rgb": {"r": 0, "g": 215, "b": 95}, "hsl": {"h": 146.511627906977, "s": 100, "l": 42}, "name": "Peridot"},
                    {"colorId": "042", "hexString": "#00d787", "rgb": {"r": 0, "g": 215, "b": 135}, "hsl": {"h": 157.674418604651, "s": 100, "l": 42}, "name": "Sea glass"},
                    {"colorId": "043", "hexString": "#00d7af", "rgb": {"r": 0, "g": 215, "b": 175}, "hsl": {"h": 168.837209302326, "s": 100, "l": 42}, "name": "Sea green"},
                    {"colorId": "044", "hexString": "#00d7d7", "rgb": {"r": 0, "g": 215, "b": 215}, "hsl": {"h": 180, "s": 100, "l": 42}, "name": "Robin egg blue"},
                    {"colorId": "045", "hexString": "#00d7ff", "rgb": {"r": 0, "g": 215, "b": 255}, "hsl": {"h": 189.411764705882, "s": 100, "l": 50}, "name": "Sky blue"},
                    {"colorId": "050", "hexString": "#00ff00", "rgb": {"r": 0, "g": 255, "b": 0}, "hsl": {"h": 120, "s": 100, "l": 50}, "name": "Virus green"},
                    {"colorId": "051", "hexString": "#00ff5f", "rgb": {"r": 0, "g": 255, "b": 95}, "hsl": {"h": 142.352941176471, "s": 100, "l": 50}, "name": "Neon green"},
                    {"colorId": "052", "hexString": "#00ff87", "rgb": {"r": 0, "g": 255, "b": 135}, "hsl": {"h": 151.764705882353, "s": 100, "l": 50}, "name": "Shamrock green"},
                    {"colorId": "053", "hexString": "#00ffaf", "rgb": {"r": 0, "g": 255, "b": 175}, "hsl": {"h": 161.176470588235, "s": 100, "l": 50}, "name": "Spring green"},
                    {"colorId": "054", "hexString": "#00ffd7", "rgb": {"r": 0, "g": 255, "b": 215}, "hsl": {"h": 170.588235294118, "s": 100, "l": 50}, "name": "Turquoise green"},
                    {"colorId": "055", "hexString": "#00ffff", "rgb": {"r": 0, "g": 255, "b": 255}, "hsl": {"h": 180, "s": 100, "l": 50}, "name": "Cyan"},
                    {"colorId": "100", "hexString": "#5f0000", "rgb": {"r": 95, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 18}, "name": "Wine red"},
                    {"colorId": "101", "hexString": "#5f005f", "rgb": {"r": 95, "g": 0, "b": 95}, "hsl": {"h": 300, "s": 100, "l": 18}, "name": "Imperial purple"},
                    {"colorId": "102", "hexString": "#5f0087", "rgb": {"r": 95, "g": 0, "b": 135}, "hsl": {"h": 282.222222222222, "s": 100, "l": 26}, "name": "Plum"},
                    {"colorId": "103", "hexString": "#5f00af", "rgb": {"r": 95, "g": 0, "b": 175}, "hsl": {"h": 272.571428571429, "s": 100, "l": 34}, "name": "Aubergine"},
                    {"colorId": "104", "hexString": "#5f00d7", "rgb": {"r": 95, "g": 0, "b": 215}, "hsl": {"h": 266.511627906977, "s": 100, "l": 42}, "name": "Royal purple"},
                    {"colorId": "105", "hexString": "#5f00ff", "rgb": {"r": 95, "g": 0, "b": 255}, "hsl": {"h": 262.352941176471, "s": 100, "l": 50}, "name": "Ultramarine"},
                    {"colorId": "110", "hexString": "#5f5f00", "rgb": {"r": 95, "g": 95, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 18}, "name": "Gingerbread"},
                    {"colorId": "111", "hexString": "#5f5f5f", "rgb": {"r": 95, "g": 95, "b": 95}, "hsl": {"h": 0, "s": 0, "l": 37}, "name": "Dark fog"},
                    {"colorId": "112", "hexString": "#5f5f87", "rgb": {"r": 95, "g": 95, "b": 135}, "hsl": {"h": 240, "s": 17, "l": 45}, "name": "Blue-grey"},
                    {"colorId": "113", "hexString": "#5f5faf", "rgb": {"r": 95, "g": 95, "b": 175}, "hsl": {"h": 240, "s": 33, "l": 52}, "name": "Twilight sky"},
                    {"colorId": "114", "hexString": "#5f5fd7", "rgb": {"r": 95, "g": 95, "b": 215}, "hsl": {"h": 240, "s": 60, "l": 60}, "name": "Twilight fog"},
                    {"colorId": "115", "hexString": "#5f5fff", "rgb": {"r": 95, "g": 95, "b": 255}, "hsl": {"h": 240, "s": 100, "l": 68}, "name": "Iris"},
                    {"colorId": "120", "hexString": "#5f8700", "rgb": {"r": 95, "g": 135, "b": 0}, "hsl": {"h": 77.7777777777778, "s": 100, "l": 26}, "name": "Avocado"},
                    {"colorId": "121", "hexString": "#5f875f", "rgb": {"r": 95, "g": 135, "b": 95}, "hsl": {"h": 120, "s": 17, "l": 45}, "name": "Fern green"},
                    {"colorId": "122", "hexString": "#5f8787", "rgb": {"r": 95, "g": 135, "b": 135}, "hsl": {"h": 180, "s": 17, "l": 45}, "name": "Slate grey"},
                    {"colorId": "123", "hexString": "#5f87af", "rgb": {"r": 95, "g": 135, "b": 175}, "hsl": {"h": 210, "s": 33, "l": 52}, "name": "Steel blue"},
                    {"colorId": "124", "hexString": "#5f87d7", "rgb": {"r": 95, "g": 135, "b": 215}, "hsl": {"h": 220, "s": 60, "l": 60}, "name": "Lake blue"},
                    {"colorId": "125", "hexString": "#5f87ff", "rgb": {"r": 95, "g": 135, "b": 255}, "hsl": {"h": 225, "s": 100, "l": 68}, "name": "Blueberry"},
                    {"colorId": "130", "hexString": "#5faf00", "rgb": {"r": 95, "g": 175, "b": 0}, "hsl": {"h": 87.4285714285714, "s": 100, "l": 34}, "name": "Basil green"},
                    {"colorId": "131", "hexString": "#5faf5f", "rgb": {"r": 95, "g": 175, "b": 95}, "hsl": {"h": 120, "s": 33, "l": 52}, "name": "Moss"},
                    {"colorId": "132", "hexString": "#5faf87", "rgb": {"r": 95, "g": 175, "b": 135}, "hsl": {"h": 150, "s": 33, "l": 52}, "name": "Tea green"},
                    {"colorId": "133", "hexString": "#5fafaf", "rgb": {"r": 95, "g": 175, "b": 175}, "hsl": {"h": 180, "s": 33, "l": 52}, "name": "Spring rain"},
                    {"colorId": "134", "hexString": "#5fafd7", "rgb": {"r": 95, "g": 175, "b": 215}, "hsl": {"h": 200, "s": 60, "l": 60}, "name": "Rain blue"},
                    {"colorId": "135", "hexString": "#5fafff", "rgb": {"r": 95, "g": 175, "b": 255}, "hsl": {"h": 210, "s": 100, "l": 68}, "name": "Morning glory"},
                    {"colorId": "140", "hexString": "#5fd700", "rgb": {"r": 95, "g": 215, "b": 0}, "hsl": {"h": 93.4883720930233, "s": 100, "l": 42}, "name": "Apple green"},
                    {"colorId": "141", "hexString": "#5fd75f", "rgb": {"r": 95, "g": 215, "b": 95}, "hsl": {"h": 120, "s": 60, "l": 60}, "name": "Myrtle green"},
                    {"colorId": "142", "hexString": "#5fd787", "rgb": {"r": 95, "g": 215, "b": 135}, "hsl": {"h": 140, "s": 60, "l": 60}, "name": "Emerald"},
                    {"colorId": "143", "hexString": "#5fd7af", "rgb": {"r": 95, "g": 215, "b": 175}, "hsl": {"h": 160, "s": 60, "l": 60}, "name": "Aquamarine"},
                    {"colorId": "144", "hexString": "#5fd7d7", "rgb": {"r": 95, "g": 215, "b": 215}, "hsl": {"h": 180, "s": 60, "l": 60}, "name": "Juniper blue"},
                    {"colorId": "145", "hexString": "#5fd7ff", "rgb": {"r": 95, "g": 215, "b": 255}, "hsl": {"h": 195, "s": 100, "l": 68}, "name": "Bluebell"},
                    {"colorId": "150", "hexString": "#5fff00", "rgb": {"r": 95, "g": 255, "b": 0}, "hsl": {"h": 97.6470588235294, "s": 100, "l": 50}, "name": "Poison green"},
                    {"colorId": "151", "hexString": "#5fff5f", "rgb": {"r": 95, "g": 255, "b": 95}, "hsl": {"h": 120, "s": 100, "l": 68}, "name": "Serpent green"},
                    {"colorId": "152", "hexString": "#5fff87", "rgb": {"r": 95, "g": 255, "b": 135}, "hsl": {"h": 135, "s": 100, "l": 68}, "name": "Sunrider"},
                    {"colorId": "153", "hexString": "#5fffaf", "rgb": {"r": 95, "g": 255, "b": 175}, "hsl": {"h": 150, "s": 100, "l": 68}, "name": "Patina green"},
                    {"colorId": "154", "hexString": "#5fffd7", "rgb": {"r": 95, "g": 255, "b": 215}, "hsl": {"h": 165, "s": 100, "l": 68}, "name": "Verdigris"},
                    {"colorId": "155", "hexString": "#5fffff", "rgb": {"r": 95, "g": 255, "b": 255}, "hsl": {"h": 180, "s": 100, "l": 68}, "name": "Neon blue"},
                    {"colorId": "200", "hexString": "#870000", "rgb": {"r": 135, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 26}, "name": "Maroon"},
                    {"colorId": "201", "hexString": "#87005f", "rgb": {"r": 135, "g": 0, "b": 95}, "hsl": {"h": 317.777777777778, "s": 100, "l": 26}, "name": "Burgundy"},
                    {"colorId": "202", "hexString": "#870087", "rgb": {"r": 135, "g": 0, "b": 135}, "hsl": {"h": 300, "s": 100, "l": 26}, "name": "Prune"},
                    {"colorId": "203", "hexString": "#8700af", "rgb": {"r": 135, "g": 0, "b": 175}, "hsl": {"h": 286.285714285714, "s": 100, "l": 34}, "name": "Purple"},
                    {"colorId": "204", "hexString": "#8700d7", "rgb": {"r": 135, "g": 0, "b": 215}, "hsl": {"h": 277.674418604651, "s": 100, "l": 42}, "name": "Grape"},
                    {"colorId": "205", "hexString": "#8700ff", "rgb": {"r": 135, "g": 0, "b": 255}, "hsl": {"h": 271.764705882353, "s": 100, "l": 50}, "name": "Amethyst"},
                    {"colorId": "210", "hexString": "#875f00", "rgb": {"r": 135, "g": 95, "b": 0}, "hsl": {"h": 42.2222222222222, "s": 100, "l": 26}, "name": "Brown"},
                    {"colorId": "211", "hexString": "#875f5f", "rgb": {"r": 135, "g": 95, "b": 95}, "hsl": {"h": 0, "s": 17, "l": 45}, "name": "Clay"},
                    {"colorId": "212", "hexString": "#875f87", "rgb": {"r": 135, "g": 95, "b": 135}, "hsl": {"h": 300, "s": 17, "l": 45}, "name": "Dusk"},
                    {"colorId": "213", "hexString": "#875faf", "rgb": {"r": 135, "g": 95, "b": 175}, "hsl": {"h": 270, "s": 33, "l": 52}, "name": "Nightshade"},
                    {"colorId": "214", "hexString": "#875fd7", "rgb": {"r": 135, "g": 95, "b": 215}, "hsl": {"h": 260, "s": 60, "l": 60}, "name": "Violet"},
                    {"colorId": "215", "hexString": "#875fff", "rgb": {"r": 135, "g": 95, "b": 255}, "hsl": {"h": 255, "s": 100, "l": 68}, "name": "Hazy violet"},
                    {"colorId": "220", "hexString": "#878700", "rgb": {"r": 135, "g": 135, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 26}, "name": "Olive"},
                    {"colorId": "221", "hexString": "#87875f", "rgb": {"r": 135, "g": 135, "b": 95}, "hsl": {"h": 60, "s": 17, "l": 45}, "name": "Bronze"},
                    {"colorId": "222", "hexString": "#878787", "rgb": {"r": 135, "g": 135, "b": 135}, "hsl": {"h": 0, "s": 0, "l": 52}, "name": "Tarnish grey"},
                    {"colorId": "223", "hexString": "#8787af", "rgb": {"r": 135, "g": 135, "b": 175}, "hsl": {"h": 240, "s": 20, "l": 60}, "name": "Shade"},
                    {"colorId": "224", "hexString": "#8787d7", "rgb": {"r": 135, "g": 135, "b": 215}, "hsl": {"h": 240, "s": 50, "l": 68}, "name": "Periwinkle"},
                    {"colorId": "225", "hexString": "#8787ff", "rgb": {"r": 135, "g": 135, "b": 255}, "hsl": {"h": 240, "s": 100, "l": 76}, "name": "Dusty purple"},
                    {"colorId": "230", "hexString": "#87af00", "rgb": {"r": 135, "g": 175, "b": 0}, "hsl": {"h": 73.7142857142857, "s": 100, "l": 34}, "name": "Olivine"},
                    {"colorId": "231", "hexString": "#87af5f", "rgb": {"r": 135, "g": 175, "b": 95}, "hsl": {"h": 90, "s": 33, "l": 52}, "name": "Asparagus"},
                    {"colorId": "232", "hexString": "#87af87", "rgb": {"r": 135, "g": 175, "b": 135}, "hsl": {"h": 120, "s": 20, "l": 60}, "name": "Pistachio"},
                    {"colorId": "233", "hexString": "#87afaf", "rgb": {"r": 135, "g": 175, "b": 175}, "hsl": {"h": 180, "s": 20, "l": 60}, "name": "Tourmaline"},
                    {"colorId": "234", "hexString": "#87afd7", "rgb": {"r": 135, "g": 175, "b": 215}, "hsl": {"h": 210, "s": 50, "l": 68}, "name": "Iceberg"},
                    {"colorId": "235", "hexString": "#87afff", "rgb": {"r": 135, "g": 175, "b": 255}, "hsl": {"h": 220, "s": 100, "l": 76}, "name": "Hazy blue"},
                    {"colorId": "240", "hexString": "#87d700", "rgb": {"r": 135, "g": 215, "b": 0}, "hsl": {"h": 82.3255813953488, "s": 100, "l": 42}, "name": "Jaundice green"},
                    {"colorId": "241", "hexString": "#87d75f", "rgb": {"r": 135, "g": 215, "b": 95}, "hsl": {"h": 100, "s": 60, "l": 60}, "name": "Lichen"},
                    {"colorId": "242", "hexString": "#87d787", "rgb": {"r": 135, "g": 215, "b": 135}, "hsl": {"h": 120, "s": 50, "l": 68}, "name": "Celadon"},
                    {"colorId": "243", "hexString": "#87d7af", "rgb": {"r": 135, "g": 215, "b": 175}, "hsl": {"h": 150, "s": 50, "l": 68}, "name": "Pastel green"},
                    {"colorId": "244", "hexString": "#87d7d7", "rgb": {"r": 135, "g": 215, "b": 215}, "hsl": {"h": 180, "s": 50, "l": 68}, "name": "Glacial blue"},
                    {"colorId": "245", "hexString": "#87d7ff", "rgb": {"r": 135, "g": 215, "b": 255}, "hsl": {"h": 200, "s": 100, "l": 76}, "name": "Pastel blue"},
                    {"colorId": "250", "hexString": "#87ff00", "rgb": {"r": 135, "g": 255, "b": 0}, "hsl": {"h": 88.2352941176471, "s": 100, "l": 50}, "name": "Toxic green"},
                    {"colorId": "251", "hexString": "#87ff5f", "rgb": {"r": 135, "g": 255, "b": 95}, "hsl": {"h": 105, "s": 100, "l": 68}, "name": "Lime"},
                    {"colorId": "252", "hexString": "#87ff87", "rgb": {"r": 135, "g": 255, "b": 135}, "hsl": {"h": 120, "s": 100, "l": 76}, "name": "Chartreuse"},
                    {"colorId": "253", "hexString": "#87ffaf", "rgb": {"r": 135, "g": 255, "b": 175}, "hsl": {"h": 140, "s": 100, "l": 76}, "name": "Mint green"},
                    {"colorId": "254", "hexString": "#87ffd7", "rgb": {"r": 135, "g": 255, "b": 215}, "hsl": {"h": 160, "s": 100, "l": 76}, "name": "Seafoam green"},
                    {"colorId": "255", "hexString": "#87ffff", "rgb": {"r": 135, "g": 255, "b": 255}, "hsl": {"h": 180, "s": 100, "l": 76}, "name": "Seafoam blue"},
                    {"colorId": "300", "hexString": "#af0000", "rgb": {"r": 175, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 34}, "name": "Scarlet"},
                    {"colorId": "301", "hexString": "#af005f", "rgb": {"r": 175, "g": 0, "b": 95}, "hsl": {"h": 327.428571428571, "s": 100, "l": 34}, "name": "Amaranth"},
                    {"colorId": "302", "hexString": "#af0087", "rgb": {"r": 175, "g": 0, "b": 135}, "hsl": {"h": 313.714285714286, "s": 100, "l": 34}, "name": "Mulberry"},
                    {"colorId": "303", "hexString": "#af00af", "rgb": {"r": 175, "g": 0, "b": 175}, "hsl": {"h": 300, "s": 100, "l": 34}, "name": "Fuchsia"},
                    {"colorId": "304", "hexString": "#af00d7", "rgb": {"r": 175, "g": 0, "b": 215}, "hsl": {"h": 288.837209302326, "s": 100, "l": 42}, "name": "Crocus"},
                    {"colorId": "305", "hexString": "#af00ff", "rgb": {"r": 175, "g": 0, "b": 255}, "hsl": {"h": 281.176470588235, "s": 100, "l": 50}, "name": "Neon purple"},
                    {"colorId": "310", "hexString": "#af5f00", "rgb": {"r": 175, "g": 95, "b": 0}, "hsl": {"h": 32.5714285714286, "s": 100, "l": 34}, "name": "Rust"},
                    {"colorId": "311", "hexString": "#af5f5f", "rgb": {"r": 175, "g": 95, "b": 95}, "hsl": {"h": 0, "s": 33, "l": 52}, "name": "Copper"},
                    {"colorId": "312", "hexString": "#af5f87", "rgb": {"r": 175, "g": 95, "b": 135}, "hsl": {"h": 330, "s": 33, "l": 52}, "name": "Desert rose"},
                    {"colorId": "313", "hexString": "#af5faf", "rgb": {"r": 175, "g": 95, "b": 175}, "hsl": {"h": 300, "s": 33, "l": 52}, "name": "Dusty rose"},
                    {"colorId": "314", "hexString": "#af5fd7", "rgb": {"r": 175, "g": 95, "b": 215}, "hsl": {"h": 280, "s": 60, "l": 60}, "name": "Rich lavender"},
                    {"colorId": "315", "hexString": "#af5fff", "rgb": {"r": 175, "g": 95, "b": 255}, "hsl": {"h": 270, "s": 100, "l": 68}, "name": "Heather"},
                    {"colorId": "320", "hexString": "#af8700", "rgb": {"r": 175, "g": 135, "b": 0}, "hsl": {"h": 46.2857142857143, "s": 100, "l": 34}, "name": "Brass"},
                    {"colorId": "321", "hexString": "#af875f", "rgb": {"r": 175, "g": 135, "b": 95}, "hsl": {"h": 30, "s": 33, "l": 52}, "name": "Dust brown"},
                    {"colorId": "322", "hexString": "#af8787", "rgb": {"r": 175, "g": 135, "b": 135}, "hsl": {"h": 0, "s": 20, "l": 60}, "name": "Rosy brown"},
                    {"colorId": "323", "hexString": "#af87af", "rgb": {"r": 175, "g": 135, "b": 175}, "hsl": {"h": 300, "s": 20, "l": 60}, "name": "Mauve"},
                    {"colorId": "324", "hexString": "#af87d7", "rgb": {"r": 175, "g": 135, "b": 215}, "hsl": {"h": 270, "s": 50, "l": 68}, "name": "Lavender"},
                    {"colorId": "325", "hexString": "#af87ff", "rgb": {"r": 175, "g": 135, "b": 255}, "hsl": {"h": 260, "s": 100, "l": 76}, "name": "Wisteria"},
                    {"colorId": "330", "hexString": "#afaf00", "rgb": {"r": 175, "g": 175, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 34}, "name": "Dull earth"},
                    {"colorId": "331", "hexString": "#afaf5f", "rgb": {"r": 175, "g": 175, "b": 95}, "hsl": {"h": 60, "s": 33, "l": 52}, "name": "Pale olive"},
                    {"colorId": "332", "hexString": "#afaf87", "rgb": {"r": 175, "g": 175, "b": 135}, "hsl": {"h": 60, "s": 20, "l": 60}, "name": "Dusty sage"},
                    {"colorId": "333", "hexString": "#afafaf", "rgb": {"r": 175, "g": 175, "b": 175}, "hsl": {"h": 0, "s": 0, "l": 68}, "name": "Talc grey"},
                    {"colorId": "334", "hexString": "#afafd7", "rgb": {"r": 175, "g": 175, "b": 215}, "hsl": {"h": 240, "s": 33, "l": 76}, "name": "Nostalgia"},
                    {"colorId": "335", "hexString": "#afafff", "rgb": {"r": 175, "g": 175, "b": 255}, "hsl": {"h": 240, "s": 100, "l": 84}, "name": "Pastel purple"},
                    {"colorId": "340", "hexString": "#afd700", "rgb": {"r": 175, "g": 215, "b": 0}, "hsl": {"h": 71.1627906976744, "s": 100, "l": 42}, "name": "Putrid green"},
                    {"colorId": "341", "hexString": "#afd75f", "rgb": {"r": 175, "g": 215, "b": 95}, "hsl": {"h": 80, "s": 60, "l": 60}, "name": "Locust"},
                    {"colorId": "342", "hexString": "#afd787", "rgb": {"r": 175, "g": 215, "b": 135}, "hsl": {"h": 90, "s": 50, "l": 68}, "name": "Pear green"},
                    {"colorId": "343", "hexString": "#afd7af", "rgb": {"r": 175, "g": 215, "b": 175}, "hsl": {"h": 120, "s": 33, "l": 76}, "name": "Opal"},
                    {"colorId": "344", "hexString": "#afd7d7", "rgb": {"r": 175, "g": 215, "b": 215}, "hsl": {"h": 180, "s": 33, "l": 76}, "name": "Mist blue"},
                    {"colorId": "345", "hexString": "#afd7ff", "rgb": {"r": 175, "g": 215, "b": 255}, "hsl": {"h": 210, "s": 100, "l": 84}, "name": "Powder blue"},
                    {"colorId": "350", "hexString": "#afff00", "rgb": {"r": 175, "g": 255, "b": 0}, "hsl": {"h": 78.8235294117647, "s": 100, "l": 50}, "name": "Acid green"},
                    {"colorId": "351", "hexString": "#afff5f", "rgb": {"r": 175, "g": 255, "b": 95}, "hsl": {"h": 90, "s": 100, "l": 68}, "name": "Lemon lime"},
                    {"colorId": "352", "hexString": "#afff87", "rgb": {"r": 175, "g": 255, "b": 135}, "hsl": {"h": 100, "s": 100, "l": 76}, "name": "Melon"},
                    {"colorId": "353", "hexString": "#afffaf", "rgb": {"r": 175, "g": 255, "b": 175}, "hsl": {"h": 120, "s": 100, "l": 84}, "name": "Firefly"},
                    {"colorId": "354", "hexString": "#afffd7", "rgb": {"r": 175, "g": 255, "b": 215}, "hsl": {"h": 150, "s": 100, "l": 84}, "name": "Sea ice"},
                    {"colorId": "355", "hexString": "#afffff", "rgb": {"r": 175, "g": 255, "b": 255}, "hsl": {"h": 180, "s": 100, "l": 84}, "name": "Glass blue"},
                    {"colorId": "400", "hexString": "#d70000", "rgb": {"r": 215, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 42}, "name": "Crimson"},
                    {"colorId": "401", "hexString": "#d7005f", "rgb": {"r": 215, "g": 0, "b": 95}, "hsl": {"h": 333.488372093023, "s": 100, "l": 42}, "name": "Ruby"},
                    {"colorId": "402", "hexString": "#d70087", "rgb": {"r": 215, "g": 0, "b": 135}, "hsl": {"h": 322.325581395349, "s": 100, "l": 42}, "name": "Raspberry"},
                    {"colorId": "403", "hexString": "#d700af", "rgb": {"r": 215, "g": 0, "b": 175}, "hsl": {"h": 311.162790697674, "s": 100, "l": 42}, "name": "Neon pink"},
                    {"colorId": "404", "hexString": "#d700d7", "rgb": {"r": 215, "g": 0, "b": 215}, "hsl": {"h": 300, "s": 100, "l": 42}, "name": "Deep magenta"},
                    {"colorId": "405", "hexString": "#d700ff", "rgb": {"r": 215, "g": 0, "b": 255}, "hsl": {"h": 290.588235294118, "s": 100, "l": 50}, "name": "Phlox"},
                    {"colorId": "410", "hexString": "#d75f00", "rgb": {"r": 215, "g": 95, "b": 0}, "hsl": {"h": 26.5116279069767, "s": 100, "l": 42}, "name": "Pumpkin"},
                    {"colorId": "411", "hexString": "#d75f5f", "rgb": {"r": 215, "g": 95, "b": 95}, "hsl": {"h": 0, "s": 60, "l": 60}, "name": "Terra cotta"},
                    {"colorId": "412", "hexString": "#d75f87", "rgb": {"r": 215, "g": 95, "b": 135}, "hsl": {"h": 340, "s": 60, "l": 60}, "name": "Antique rose"},
                    {"colorId": "413", "hexString": "#d75faf", "rgb": {"r": 215, "g": 95, "b": 175}, "hsl": {"h": 320, "s": 60, "l": 60}, "name": "Pink"},
                    {"colorId": "414", "hexString": "#d75fd7", "rgb": {"r": 215, "g": 95, "b": 215}, "hsl": {"h": 300, "s": 60, "l": 60}, "name": "Foxglove"},
                    {"colorId": "415", "hexString": "#d75fff", "rgb": {"r": 215, "g": 95, "b": 255}, "hsl": {"h": 285, "s": 100, "l": 68}, "name": "Verbena"},
                    {"colorId": "420", "hexString": "#d78700", "rgb": {"r": 215, "g": 135, "b": 0}, "hsl": {"h": 37.6744186046512, "s": 100, "l": 42}, "name": "Honey"},
                    {"colorId": "421", "hexString": "#d7875f", "rgb": {"r": 215, "g": 135, "b": 95}, "hsl": {"h": 20, "s": 60, "l": 60}, "name": "Duststorm"},
                    {"colorId": "422", "hexString": "#d78787", "rgb": {"r": 215, "g": 135, "b": 135}, "hsl": {"h": 0, "s": 50, "l": 68}, "name": "Peach"},
                    {"colorId": "423", "hexString": "#d787af", "rgb": {"r": 215, "g": 135, "b": 175}, "hsl": {"h": 330, "s": 50, "l": 68}, "name": "Pink pearl"},
                    {"colorId": "424", "hexString": "#d787d7", "rgb": {"r": 215, "g": 135, "b": 215}, "hsl": {"h": 300, "s": 50, "l": 68}, "name": "Orchid"},
                    {"colorId": "425", "hexString": "#d787ff", "rgb": {"r": 215, "g": 135, "b": 255}, "hsl": {"h": 280, "s": 100, "l": 76}, "name": "Heliotrope"},
                    {"colorId": "430", "hexString": "#d7af00", "rgb": {"r": 215, "g": 175, "b": 0}, "hsl": {"h": 48.8372093023256, "s": 100, "l": 42}, "name": "Goldenrod"},
                    {"colorId": "431", "hexString": "#d7af5f", "rgb": {"r": 215, "g": 175, "b": 95}, "hsl": {"h": 40, "s": 60, "l": 60}, "name": "Fawn"},
                    {"colorId": "432", "hexString": "#d7af87", "rgb": {"r": 215, "g": 175, "b": 135}, "hsl": {"h": 30, "s": 50, "l": 68}, "name": "Tan"},
                    {"colorId": "433", "hexString": "#d7afaf", "rgb": {"r": 215, "g": 175, "b": 175}, "hsl": {"h": 0, "s": 33, "l": 76}, "name": "Pink lemonade"},
                    {"colorId": "434", "hexString": "#d7afd7", "rgb": {"r": 215, "g": 175, "b": 215}, "hsl": {"h": 300, "s": 33, "l": 76}, "name": "Thistle"},
                    {"colorId": "435", "hexString": "#d7afff", "rgb": {"r": 215, "g": 175, "b": 255}, "hsl": {"h": 270, "s": 100, "l": 84}, "name": "Lilac"},
                    {"colorId": "440", "hexString": "#d7d700", "rgb": {"r": 215, "g": 215, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 42}, "name": "Gold"},
                    {"colorId": "441", "hexString": "#d7d75f", "rgb": {"r": 215, "g": 215, "b": 95}, "hsl": {"h": 60, "s": 60, "l": 60}, "name": "Butterscotch"},
                    {"colorId": "442", "hexString": "#d7d787", "rgb": {"r": 215, "g": 215, "b": 135}, "hsl": {"h": 60, "s": 50, "l": 68}, "name": "Buttercream"},
                    {"colorId": "443", "hexString": "#d7d7af", "rgb": {"r": 215, "g": 215, "b": 175}, "hsl": {"h": 60, "s": 33, "l": 76}, "name": "Sandstone"},
                    {"colorId": "444", "hexString": "#d7d7d7", "rgb": {"r": 215, "g": 215, "b": 215}, "hsl": {"h": 0, "s": 0, "l": 84}, "name": "Lace grey"},
                    {"colorId": "445", "hexString": "#d7d7ff", "rgb": {"r": 215, "g": 215, "b": 255}, "hsl": {"h": 240, "s": 100, "l": 92}, "name": "Crystal blue"},
                    {"colorId": "450", "hexString": "#d7ff00", "rgb": {"r": 215, "g": 255, "b": 0}, "hsl": {"h": 69.4117647058823, "s": 100, "l": 50}, "name": "Neon yellow"},
                    {"colorId": "451", "hexString": "#d7ff5f", "rgb": {"r": 215, "g": 255, "b": 95}, "hsl": {"h": 75, "s": 100, "l": 68}, "name": "Lemonade"},
                    {"colorId": "452", "hexString": "#d7ff87", "rgb": {"r": 215, "g": 255, "b": 135}, "hsl": {"h": 80, "s": 100, "l": 76}, "name": "Sunlight"},
                    {"colorId": "453", "hexString": "#d7ffaf", "rgb": {"r": 215, "g": 255, "b": 175}, "hsl": {"h": 90, "s": 100, "l": 84}, "name": "Daisy yellow"},
                    {"colorId": "454", "hexString": "#d7ffd7", "rgb": {"r": 215, "g": 255, "b": 215}, "hsl": {"h": 120, "s": 100, "l": 92}, "name": "Canvas"},
                    {"colorId": "455", "hexString": "#d7ffff", "rgb": {"r": 215, "g": 255, "b": 255}, "hsl": {"h": 180, "s": 100, "l": 92}, "name": "Frost white"},
                    {"colorId": "500", "hexString": "#ff0000", "rgb": {"r": 255, "g": 0, "b": 0}, "hsl": {"h": 0, "s": 100, "l": 50}, "name": "Red"},
                    {"colorId": "501", "hexString": "#ff005f", "rgb": {"r": 255, "g": 0, "b": 95}, "hsl": {"h": 337.647058823529, "s": 100, "l": 50}, "name": "Watermelon"},
                    {"colorId": "502", "hexString": "#ff0087", "rgb": {"r": 255, "g": 0, "b": 135}, "hsl": {"h": 328.235294117647, "s": 100, "l": 50}, "name": "Rose"},
                    {"colorId": "503", "hexString": "#ff00af", "rgb": {"r": 255, "g": 0, "b": 175}, "hsl": {"h": 318.823529411765, "s": 100, "l": 50}, "name": "Peony"},
                    {"colorId": "504", "hexString": "#ff00d7", "rgb": {"r": 255, "g": 0, "b": 215}, "hsl": {"h": 309.411764705882, "s": 100, "l": 50}, "name": "Magenta"},
                    {"colorId": "505", "hexString": "#ff00ff", "rgb": {"r": 255, "g": 0, "b": 255}, "hsl": {"h": 300, "s": 100, "l": 50}, "name": "Hot pink"},
                    {"colorId": "510", "hexString": "#ff5f00", "rgb": {"r": 255, "g": 95, "b": 0}, "hsl": {"h": 22.3529411764706, "s": 100, "l": 50}, "name": "Flame"},
                    {"colorId": "511", "hexString": "#ff5f5f", "rgb": {"r": 255, "g": 95, "b": 95}, "hsl": {"h": 0, "s": 100, "l": 68}, "name": "Strawberry"},
                    {"colorId": "512", "hexString": "#ff5f87", "rgb": {"r": 255, "g": 95, "b": 135}, "hsl": {"h": 345, "s": 100, "l": 68}, "name": "Salmon pink"},
                    {"colorId": "513", "hexString": "#ff5faf", "rgb": {"r": 255, "g": 95, "b": 175}, "hsl": {"h": 330, "s": 100, "l": 68}, "name": "Tea rose"},
                    {"colorId": "514", "hexString": "#ff5fd7", "rgb": {"r": 255, "g": 95, "b": 215}, "hsl": {"h": 315, "s": 100, "l": 68}, "name": "Sweet pea"},
                    {"colorId": "515", "hexString": "#ff5fff", "rgb": {"r": 255, "g": 95, "b": 255}, "hsl": {"h": 300, "s": 100, "l": 68}, "name": "Bubblegum"},
                    {"colorId": "520", "hexString": "#ff8700", "rgb": {"r": 255, "g": 135, "b": 0}, "hsl": {"h": 31.7647058823529, "s": 100, "l": 50}, "name": "Orange"},
                    {"colorId": "521", "hexString": "#ff875f", "rgb": {"r": 255, "g": 135, "b": 95}, "hsl": {"h": 15, "s": 100, "l": 68}, "name": "Sunset"},
                    {"colorId": "522", "hexString": "#ff8787", "rgb": {"r": 255, "g": 135, "b": 135}, "hsl": {"h": 0, "s": 100, "l": 76}, "name": "Tangerine"},
                    {"colorId": "523", "hexString": "#ff87af", "rgb": {"r": 255, "g": 135, "b": 175}, "hsl": {"h": 340, "s": 100, "l": 76}, "name": "Coral"},
                    {"colorId": "524", "hexString": "#ff87d7", "rgb": {"r": 255, "g": 135, "b": 215}, "hsl": {"h": 320, "s": 100, "l": 76}, "name": "Sherbet"},
                    {"colorId": "525", "hexString": "#ff87ff", "rgb": {"r": 255, "g": 135, "b": 255}, "hsl": {"h": 300, "s": 100, "l": 76}, "name": "Camellia"},
                    {"colorId": "530", "hexString": "#ffaf00", "rgb": {"r": 255, "g": 175, "b": 0}, "hsl": {"h": 41.1764705882353, "s": 100, "l": 50}, "name": "Ochre"},
                    {"colorId": "531", "hexString": "#ffaf5f", "rgb": {"r": 255, "g": 175, "b": 95}, "hsl": {"h": 30, "s": 100, "l": 68}, "name": "Sand"},
                    {"colorId": "532", "hexString": "#ffaf87", "rgb": {"r": 255, "g": 175, "b": 135}, "hsl": {"h": 20, "s": 100, "l": 76}, "name": "Dawn"},
                    {"colorId": "533", "hexString": "#ffafaf", "rgb": {"r": 255, "g": 175, "b": 175}, "hsl": {"h": 0, "s": 100, "l": 84}, "name": "Blush pink"},
                    {"colorId": "534", "hexString": "#ffafd7", "rgb": {"r": 255, "g": 175, "b": 215}, "hsl": {"h": 330, "s": 100, "l": 84}, "name": "Rose quartz"},
                    {"colorId": "535", "hexString": "#ffafff", "rgb": {"r": 255, "g": 175, "b": 255}, "hsl": {"h": 300, "s": 100, "l": 84}, "name": "Pastel pink"},
                    {"colorId": "540", "hexString": "#ffd700", "rgb": {"r": 255, "g": 215, "b": 0}, "hsl": {"h": 50.5882352941176, "s": 100, "l": 50}, "name": "Candlelight"},
                    {"colorId": "541", "hexString": "#ffd75f", "rgb": {"r": 255, "g": 215, "b": 95}, "hsl": {"h": 45, "s": 100, "l": 68}, "name": "Mustard"},
                    {"colorId": "542", "hexString": "#ffd787", "rgb": {"r": 255, "g": 215, "b": 135}, "hsl": {"h": 40, "s": 100, "l": 76}, "name": "Marigold"},
                    {"colorId": "543", "hexString": "#ffd7af", "rgb": {"r": 255, "g": 215, "b": 175}, "hsl": {"h": 30, "s": 100, "l": 84}, "name": "Beige"},
                    {"colorId": "544", "hexString": "#ffd7d7", "rgb": {"r": 255, "g": 215, "b": 215}, "hsl": {"h": 0, "s": 100, "l": 92}, "name": "Primrose"},
                    {"colorId": "545", "hexString": "#ffd7ff", "rgb": {"r": 255, "g": 215, "b": 255}, "hsl": {"h": 300, "s": 100, "l": 92}, "name": "Powder pink"},
                    {"colorId": "550", "hexString": "#ffff00", "rgb": {"r": 255, "g": 255, "b": 0}, "hsl": {"h": 60, "s": 100, "l": 50}, "name": "Yellow"},
                    {"colorId": "551", "hexString": "#ffff5f", "rgb": {"r": 255, "g": 255, "b": 95}, "hsl": {"h": 60, "s": 100, "l": 68}, "name": "Lemon"},
                    {"colorId": "552", "hexString": "#ffff87", "rgb": {"r": 255, "g": 255, "b": 135}, "hsl": {"h": 60, "s": 100, "l": 76}, "name": "Canary"},
                    {"colorId": "553", "hexString": "#ffffaf", "rgb": {"r": 255, "g": 255, "b": 175}, "hsl": {"h": 60, "s": 100, "l": 84}, "name": "Vanilla"},
                    {"colorId": "554", "hexString": "#ffffd7", "rgb": {"r": 255, "g": 255, "b": 215}, "hsl": {"h": 60, "s": 100, "l": 92}, "name": "Ivory"},
                    {"colorId": "555", "hexString": "#ffffff", "rgb": {"r": 255, "g": 255, "b": 255}, "hsl": {"h": 0, "s": 0, "l": 100}, "name": "White"},
                    {"colorId": "=a", "hexString": "#080808", "rgb": {"r": 8, "g": 8, "b": 8}, "hsl": {"h": 0, "s": 0, "l": 3}, "name": "Too Black"},
                    {"colorId": "=b", "hexString": "#121212", "rgb": {"r": 18, "g": 18, "b": 18}, "hsl": {"h": 0, "s": 0, "l": 7}, "name": "Too Black"},
                    {"colorId": "=c", "hexString": "#1c1c1c", "rgb": {"r": 28, "g": 28, "b": 28}, "hsl": {"h": 0, "s": 0, "l": 10}, "name": "Too Black"},
                    {"colorId": "=d", "hexString": "#262626", "rgb": {"r": 38, "g": 38, "b": 38}, "hsl": {"h": 0, "s": 0, "l": 14}, "name": "Too Black"},
                    {"colorId": "=e", "hexString": "#303030", "rgb": {"r": 48, "g": 48, "b": 48}, "hsl": {"h": 0, "s": 0, "l": 18}, "name": "Black"},
                    {"colorId": "=f", "hexString": "#3a3a3a", "rgb": {"r": 58, "g": 58, "b": 58}, "hsl": {"h": 0, "s": 0, "l": 22}, "name": "Obsidian"},
                    {"colorId": "=g", "hexString": "#444444", "rgb": {"r": 68, "g": 68, "b": 68}, "hsl": {"h": 0, "s": 0, "l": 26}, "name": "Onyx"},
                    {"colorId": "=h", "hexString": "#4e4e4e", "rgb": {"r": 78, "g": 78, "b": 78}, "hsl": {"h": 0, "s": 0, "l": 30}, "name": "Charcoal"},
                    {"colorId": "=i", "hexString": "#585858", "rgb": {"r": 88, "g": 88, "b": 88}, "hsl": {"h": 0, "s": 0, "l": 34}, "name": "Graphite"},
                    {"colorId": "=j", "hexString": "#626262", "rgb": {"r": 98, "g": 98, "b": 98}, "hsl": {"h": 0, "s": 0, "l": 37}, "name": "Granite grey"},
                    {"colorId": "=k", "hexString": "#6c6c6c", "rgb": {"r": 108, "g": 108, "b": 108}, "hsl": {"h": 0, "s": 0, "l": 40}, "name": "Storm grey"},
                    {"colorId": "=l", "hexString": "#767676", "rgb": {"r": 118, "g": 118, "b": 118}, "hsl": {"h": 0, "s": 0, "l": 46}, "name": "Nickel"},
                    {"colorId": "=m", "hexString": "#808080", "rgb": {"r": 128, "g": 128, "b": 128}, "hsl": {"h": 0, "s": 0, "l": 50}, "name": "Grey"},
                    {"colorId": "=n", "hexString": "#8a8a8a", "rgb": {"r": 138, "g": 138, "b": 138}, "hsl": {"h": 0, "s": 0, "l": 54}, "name": "Grey"},
                    {"colorId": "=o", "hexString": "#949494", "rgb": {"r": 148, "g": 148, "b": 148}, "hsl": {"h": 0, "s": 0, "l": 58}, "name": "Grey"},
                    {"colorId": "=p", "hexString": "#9e9e9e", "rgb": {"r": 158, "g": 158, "b": 158}, "hsl": {"h": 0, "s": 0, "l": 61}, "name": "Grey"},
                    {"colorId": "=q", "hexString": "#a8a8a8", "rgb": {"r": 168, "g": 168, "b": 168}, "hsl": {"h": 0, "s": 0, "l": 65}, "name": "Dove grey"},
                    {"colorId": "=r", "hexString": "#b2b2b2", "rgb": {"r": 178, "g": 178, "b": 178}, "hsl": {"h": 0, "s": 0, "l": 69}, "name": "Smoke"},
                    {"colorId": "=s", "hexString": "#bcbcbc", "rgb": {"r": 188, "g": 188, "b": 188}, "hsl": {"h": 0, "s": 0, "l": 73}, "name": "Quicksilver"},
                    {"colorId": "=t", "hexString": "#c6c6c6", "rgb": {"r": 198, "g": 198, "b": 198}, "hsl": {"h": 0, "s": 0, "l": 77}, "name": "Silver"},
                    {"colorId": "=u", "hexString": "#d0d0d0", "rgb": {"r": 208, "g": 208, "b": 208}, "hsl": {"h": 0, "s": 0, "l": 81}, "name": "Marble"},
                    {"colorId": "=v", "hexString": "#dadada", "rgb": {"r": 218, "g": 218, "b": 218}, "hsl": {"h": 0, "s": 0, "l": 85}, "name": "Moonstone"},
                    {"colorId": "=y", "hexString": "#e4e4e4", "rgb": {"r": 228, "g": 228, "b": 228}, "hsl": {"h": 0, "s": 0, "l": 89}, "name": "Pearl"},
                    {"colorId": "=z", "hexString": "#eeeeee", "rgb": {"r": 238, "g": 238, "b": 238}, "hsl": {"h": 0, "s": 0, "l": 93}, "name": "Alabaster"}]


def mix_colors(mix_list):
    # mix_list = [colorcode1, colorcode2, colorcode3 etc - looking for the COLOR CODES here!]

    # Colors: All the hue/saturation/lightness color info of the color codes in the list
    colors = [x.get('hsl') for x in xterm_color_data if x.get('colorId') in mix_list]
    color_names = [x.get('name') for x in xterm_color_data if x.get('colorId') in mix_list]
    if len(set(color_names)) == 1:
        # if the colors are the same
        return color_names[0], mix_list[0]
    num_colors = len(colors) + 1
    # The calculation to get the 'mixed color' information...
    x, y, z = 0, 0, 0

    for c in colors:
        hue = c.get('h')
        saturation = c.get('s')
        lightness = c.get('l')
        x += math.cos(hue / 180 * math.pi) * saturation
        y += math.sin(hue / 180 * math.pi) * saturation
        z += lightness

    x = x / num_colors
    y = y / num_colors
    z = z / num_colors

    new_hue = math.atan2(y, x) * 180 / math.pi
    if new_hue < 0:
        new_hue = new_hue + 360
    new_sat = round(math.sqrt(x * x + y * y))
    new_light = round(z)
    if new_hue:
        hue_min = max(1, round(new_hue - 10))
    else:
        hue_min = 0

    # Get the closest color to these values...
    potential_colors = []
    potential_color_names = ''
    saturation_diff = 100
    lightness_diff = 100
    closest_match = ''
    color_code = "x"

    for potential_color in xterm_color_data:
        hsl = potential_color.get('hsl')
        if hsl.get('h') in range(hue_min, round(new_hue + 10)):
            # Ensure you're only adding closer matches
            temp_saturation_diff = abs(hsl.get('s') - new_sat)
            if temp_saturation_diff > saturation_diff:
                continue
            temp_lightness_diff = abs(hsl.get('l') - new_light)
            if temp_lightness_diff > lightness_diff:
                continue
            # Future matches will only be closer
            saturation_diff = temp_saturation_diff
            lightness_diff = temp_lightness_diff
            potential_colors.append(potential_color)
            closest_match = potential_color.get('name')
            color_code = potential_color.get('colorId')
            potential_color_names += closest_match

    return closest_match, color_code
