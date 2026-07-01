"""
disease_info.py — Disease Information, Symptoms & Treatment Recommendations
for all 38 PlantVillage dataset classes.
"""

DISEASE_INFO = {
    # ─── APPLE ────────────────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "plant": "Apple",
        "disease": "Apple Scab",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Apple scab is a fungal disease caused by Venturia inaequalis. "
            "It is one of the most common and economically important apple diseases worldwide."
        ),
        "symptoms": [
            "Olive-green to black lesions on leaves",
            "Velvety or corky scab-like lesions on fruit",
            "Premature leaf drop in severe infections",
            "Distorted or cracked fruit surface",
        ],
        "treatment": [
            "Apply fungicides (captan, myclobutanil, or mancozeb) preventively",
            "Remove and destroy infected fallen leaves",
            "Prune trees to improve air circulation",
            "Plant resistant apple varieties where possible",
        ],
        "prevention": "Avoid overhead irrigation; apply dormant sprays in early spring.",
    },
    "Apple___Black_rot": {
        "plant": "Apple",
        "disease": "Black Rot",
        "healthy": False,
        "severity": "High",
        "description": (
            "Black rot is caused by the fungus Botryosphaeria obtusa. "
            "It affects fruit, leaves, and bark, causing significant yield loss."
        ),
        "symptoms": [
            "Purple spots on leaves that enlarge with yellow halos",
            "Rotten brown to black areas on fruit",
            "Cankers on branches and limbs",
            "Mummified fruit remaining on the tree",
        ],
        "treatment": [
            "Prune out dead and cankered wood",
            "Remove mummified fruit from the tree and ground",
            "Apply copper-based fungicides during the growing season",
            "Improve orchard sanitation by removing debris",
        ],
        "prevention": "Maintain tree vigor through proper fertilization and irrigation.",
    },
    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "disease": "Cedar Apple Rust",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Cedar apple rust is caused by Gymnosporangium juniperi-virginianae. "
            "It requires two hosts: apple and eastern red cedar/juniper to complete its life cycle."
        ),
        "symptoms": [
            "Bright orange or yellow spots on upper leaf surface",
            "Tube-like structures (aecia) on underside of leaves",
            "Infected fruit shows orange spots and distortion",
            "Defoliation in severe cases",
        ],
        "treatment": [
            "Apply myclobutanil or mancozeb fungicides at bud break",
            "Remove nearby juniper/cedar trees if feasible",
            "Plant rust-resistant apple varieties",
            "Apply protective fungicides every 7–10 days during wet spring weather",
        ],
        "prevention": "Create physical distance between apple trees and juniper hosts.",
    },
    "Apple___healthy": {
        "plant": "Apple",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This apple leaf appears healthy with no signs of disease or infection.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Continue regular monitoring, proper irrigation, and balanced fertilization.",
    },

    # ─── BLUEBERRY ────────────────────────────────────────────────────────────
    "Blueberry___healthy": {
        "plant": "Blueberry",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This blueberry leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Maintain acidic soil (pH 4.5–5.5), adequate irrigation, and annual pruning.",
    },

    # ─── CHERRY ────────────────────────────────────────────────────────────────
    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry",
        "disease": "Powdery Mildew",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Powdery mildew on cherry is caused by Podosphaera clandestina. "
            "It appears as a white powdery coating on leaves and young shoots."
        ),
        "symptoms": [
            "White or gray powdery coating on leaves",
            "Distorted or stunted young leaves and shoots",
            "Premature leaf drop",
            "Reduced fruit quality and yield",
        ],
        "treatment": [
            "Apply sulfur-based or potassium bicarbonate fungicides",
            "Use neem oil sprays as an organic option",
            "Prune infected shoots and improve air circulation",
            "Avoid excessive nitrogen fertilization",
        ],
        "prevention": "Choose resistant varieties; avoid dense planting.",
    },
    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This cherry leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Maintain good orchard hygiene and monitor for pests regularly.",
    },

    # ─── CORN (MAIZE) ─────────────────────────────────────────────────────────
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn (Maize)",
        "disease": "Gray Leaf Spot (Cercospora Leaf Spot)",
        "healthy": False,
        "severity": "High",
        "description": (
            "Gray leaf spot is caused by Cercospora zeae-maydis. "
            "It is one of the most yield-limiting diseases of corn worldwide."
        ),
        "symptoms": [
            "Tan to gray rectangular lesions parallel to leaf veins",
            "Lesions have distinct parallel edges",
            "Severe blighting and premature death of leaves",
            "Reduced photosynthesis and grain fill",
        ],
        "treatment": [
            "Apply strobilurin or triazole fungicides at early tasseling",
            "Plant resistant hybrid varieties",
            "Rotate crops with non-host plants",
            "Reduce crop residue through tillage",
        ],
        "prevention": "Avoid continuous corn planting; use crop rotation.",
    },
    "Corn_(maize)___Common_rust_": {
        "plant": "Corn (Maize)",
        "disease": "Common Rust",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Common rust is caused by Puccinia sorghi. "
            "It develops rapidly under cool, moist conditions."
        ),
        "symptoms": [
            "Small, round to elongated brick-red pustules on both leaf surfaces",
            "Pustules turn dark brown/black as the season progresses",
            "Yellowing and death of heavily infected leaves",
            "Premature senescence",
        ],
        "treatment": [
            "Apply fungicides (propiconazole, azoxystrobin) at first sign of infection",
            "Plant resistant corn hybrids",
            "Early planting to avoid peak rust season",
        ],
        "prevention": "Scout fields regularly in summer; monitor weather for favorable rust conditions.",
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)",
        "disease": "Northern Leaf Blight",
        "healthy": False,
        "severity": "High",
        "description": (
            "Northern leaf blight is caused by Exserohilum turcicum. "
            "It can cause significant yield losses in susceptible hybrids."
        ),
        "symptoms": [
            "Large, cigar-shaped gray-green to tan lesions",
            "Lesions range from 1–6 inches long",
            "Blighted leaves appear scorched and gray-green",
            "Severe infection can cause complete leaf blighting",
        ],
        "treatment": [
            "Apply foliar fungicides (triazoles, strobilurins) at tasseling",
            "Use resistant hybrids with Ht gene resistance",
            "Practice crop rotation and residue management",
        ],
        "prevention": "Select resistant hybrid varieties adapted to your region.",
    },
    "Corn_(maize)___healthy": {
        "plant": "Corn (Maize)",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This corn leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Maintain proper plant spacing, balanced fertilization, and monitor for early pest signs.",
    },

    # ─── GRAPE ────────────────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "plant": "Grape",
        "disease": "Black Rot",
        "healthy": False,
        "severity": "High",
        "description": (
            "Grape black rot is caused by Guignardia bidwellii. "
            "It can destroy entire crops under wet conditions."
        ),
        "symptoms": [
            "Reddish-brown circular lesions on leaves with dark borders",
            "Black shriveled mummified berries (raisins)",
            "Lesions on shoots and tendrils",
            "Tiny black fruiting bodies (pycnidia) within leaf lesions",
        ],
        "treatment": [
            "Apply mancozeb, myclobutanil, or captan starting at bud break",
            "Remove and destroy mummified berries and infected shoot tips",
            "Prune vines for open canopy and good air circulation",
            "Spray every 7–14 days during wet weather",
        ],
        "prevention": "Remove all infected plant material; maintain proper vine spacing.",
    },
    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape",
        "disease": "Esca (Black Measles)",
        "healthy": False,
        "severity": "High",
        "description": (
            "Esca is a complex wood disease of grapevines caused by multiple fungal pathogens "
            "including Phaeomoniella chlamydospora and Phaeoacremonium species."
        ),
        "symptoms": [
            "Tiger-striped yellowing pattern on leaves (interveinal chlorosis)",
            "Black or reddish-brown spots on berries",
            "Sudden wilting and death of entire vine shoots ('apoplexy')",
            "Internal wood decay with white spongy rot",
        ],
        "treatment": [
            "No effective chemical cure exists; focus on prevention",
            "Remove and destroy heavily infected vines",
            "Protect pruning wounds with fungicide or wound sealant",
            "Avoid excessive pruning stress",
        ],
        "prevention": "Disinfect pruning tools; make clean cuts during dry weather.",
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape",
        "disease": "Leaf Blight (Isariopsis Leaf Spot)",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Caused by Pseudocercospora vitis (formerly Isariopsis clavispora). "
            "Most severe in hot, humid growing regions."
        ),
        "symptoms": [
            "Irregular dark brown lesions with yellow halos on leaves",
            "Lesions may coalesce causing large necrotic areas",
            "Premature defoliation",
            "Dark brown spots on berries in severe cases",
        ],
        "treatment": [
            "Apply copper-based fungicides or mancozeb",
            "Remove infected leaves and improve air circulation",
            "Avoid overhead irrigation",
        ],
        "prevention": "Maintain well-drained soil; apply preventive fungicide sprays.",
    },
    "Grape___healthy": {
        "plant": "Grape",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This grape leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Maintain proper vine training, pruning, and integrated pest management.",
    },

    # ─── ORANGE ────────────────────────────────────────────────────────────────
    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange",
        "disease": "Huanglongbing (Citrus Greening)",
        "healthy": False,
        "severity": "Critical",
        "description": (
            "Citrus greening (HLB) is caused by the bacterium Candidatus Liberibacter asiaticus "
            "and transmitted by the Asian citrus psyllid. It is the most devastating citrus disease worldwide."
        ),
        "symptoms": [
            "Asymmetric blotchy yellow mottling on leaves",
            "Small, misshapen, bitter fruit with green color at base",
            "Fruit drop before maturity",
            "Twig dieback and general tree decline",
        ],
        "treatment": [
            "No cure exists; remove and destroy infected trees",
            "Control the Asian citrus psyllid vector with insecticides",
            "Use certified disease-free nursery stock",
            "Implement area-wide vector management programs",
        ],
        "prevention": "Use psyllid-resistant rootstocks; quarantine new plant material.",
    },

    # ─── PEACH ────────────────────────────────────────────────────────────────
    "Peach___Bacterial_spot": {
        "plant": "Peach",
        "disease": "Bacterial Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Bacterial spot on peach is caused by Xanthomonas arboricola pv. pruni. "
            "It affects leaves, twigs, and fruit."
        ),
        "symptoms": [
            "Water-soaked spots on leaves that turn purple-brown",
            "Holes or 'shot holes' in leaves where lesions drop out",
            "Sunken, water-soaked spots on fruit",
            "Twig cankers with dark, water-soaked appearance",
        ],
        "treatment": [
            "Apply copper-based bactericides from bud break through early summer",
            "Avoid overhead irrigation",
            "Prune out infected twigs during dry weather",
            "Plant resistant peach varieties",
        ],
        "prevention": "Maintain good air circulation; avoid excess nitrogen fertilization.",
    },
    "Peach___healthy": {
        "plant": "Peach",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This peach leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Regular pruning, pest monitoring, and balanced nutrition are recommended.",
    },

    # ─── PEPPER (BELL) ────────────────────────────────────────────────────────
    "Pepper,_bell___Bacterial_spot": {
        "plant": "Bell Pepper",
        "disease": "Bacterial Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Bacterial spot on pepper is caused by Xanthomonas campestris pv. vesicatoria. "
            "It is favored by warm, wet conditions."
        ),
        "symptoms": [
            "Small, water-soaked spots on leaves that turn brown with yellow halos",
            "Raised, scab-like lesions on fruit",
            "Defoliation in severe infections",
            "Stem and fruit infections causing significant crop loss",
        ],
        "treatment": [
            "Apply copper hydroxide or copper sulfate sprays",
            "Use disease-free certified seeds and transplants",
            "Rotate crops — avoid planting peppers or tomatoes in the same field",
            "Remove and destroy infected plant debris",
        ],
        "prevention": "Use drip irrigation; avoid working in fields when plants are wet.",
    },
    "Pepper,_bell___healthy": {
        "plant": "Bell Pepper",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This bell pepper leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Maintain consistent watering, good drainage, and monitor for aphids and whiteflies.",
    },

    # ─── POTATO ────────────────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "plant": "Potato",
        "disease": "Early Blight",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Early blight is caused by Alternaria solani. "
            "It typically starts on older leaves and moves upward."
        ),
        "symptoms": [
            "Dark brown to black lesions with concentric rings (target-board pattern)",
            "Yellowing of tissue surrounding lesions",
            "Premature defoliation starting from lower leaves",
            "Sunken, dark, leathery lesions on tubers",
        ],
        "treatment": [
            "Apply chlorothalonil, mancozeb, or copper-based fungicides",
            "Remove and destroy infected plant material",
            "Ensure proper plant nutrition (nitrogen levels)",
            "Irrigate in the morning to allow foliage to dry",
        ],
        "prevention": "Use certified disease-free seed potatoes; practice 3-year crop rotation.",
    },
    "Potato___Late_blight": {
        "plant": "Potato",
        "disease": "Late Blight",
        "healthy": False,
        "severity": "Critical",
        "description": (
            "Late blight is caused by the oomycete Phytophthora infestans. "
            "It was responsible for the Irish Potato Famine (1840s) and remains a devastating crop disease."
        ),
        "symptoms": [
            "Water-soaked pale green to brown lesions on leaves",
            "White fuzzy sporulation on underside of leaves in humid conditions",
            "Lesions rapidly expand and turn brown-black",
            "Brown to reddish-brown firm rot in tubers",
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, metalaxyl, cymoxanil) immediately upon detection",
            "Destroy infected plants completely — do not compost",
            "Ensure good field drainage",
            "Hill-up potato rows to protect tubers",
        ],
        "prevention": "Plant resistant varieties; monitor weather for blight-favorable conditions (cool, wet).",
    },
    "Potato___healthy": {
        "plant": "Potato",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This potato leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Use certified seed potatoes, practice crop rotation, and scout for pests regularly.",
    },

    # ─── RASPBERRY ────────────────────────────────────────────────────────────
    "Raspberry___healthy": {
        "plant": "Raspberry",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This raspberry leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Prune canes annually, maintain proper spacing, and monitor for cane borers.",
    },

    # ─── SOYBEAN ────────────────────────────────────────────────────────────────
    "Soybean___healthy": {
        "plant": "Soybean",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This soybean leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Rotate with non-legume crops; monitor for aphids and soybean cyst nematode.",
    },

    # ─── SQUASH ────────────────────────────────────────────────────────────────
    "Squash___Powdery_mildew": {
        "plant": "Squash",
        "disease": "Powdery Mildew",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Powdery mildew on squash is caused by Podosphaera xanthii or Erysiphe cichoracearum. "
            "It thrives in warm, dry conditions with high humidity."
        ),
        "symptoms": [
            "White powdery coating on upper and lower leaf surfaces",
            "Yellowing and browning of infected leaves",
            "Premature leaf death",
            "Reduced fruit size and quality",
        ],
        "treatment": [
            "Apply potassium bicarbonate, neem oil, or sulfur-based fungicides",
            "Use kaolin clay sprays to reduce spore germination",
            "Remove severely infected leaves",
            "Improve air circulation through proper plant spacing",
        ],
        "prevention": "Water in the morning; avoid overhead irrigation.",
    },

    # ─── STRAWBERRY ────────────────────────────────────────────────────────────
    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "disease": "Leaf Scorch",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Strawberry leaf scorch is caused by Diplocarpon earliana. "
            "It overwinters in infected leaves and spreads through rain splash."
        ),
        "symptoms": [
            "Irregular purple spots on upper leaf surface",
            "Centers of spots turn gray or white as they age",
            "Severe infections cause leaf tips and margins to appear scorched",
            "Reduced plant vigor and fruit yield",
        ],
        "treatment": [
            "Apply captan or myclobutanil fungicides",
            "Remove old and infected leaves after harvest",
            "Renovate strawberry beds annually",
            "Plant resistant varieties",
        ],
        "prevention": "Use drip irrigation; mulch around plants to reduce rain splash.",
    },
    "Strawberry___healthy": {
        "plant": "Strawberry",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This strawberry leaf appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Renovate beds annually, use certified plants, and control spider mites.",
    },

    # ─── TOMATO ────────────────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "disease": "Bacterial Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Caused by Xanthomonas species. It affects leaves, stems, and fruit, "
            "particularly under warm, wet conditions."
        ),
        "symptoms": [
            "Small, water-soaked spots on leaves with yellow halos",
            "Spots turn brown to black and may fall out (shot holes)",
            "Raised, scab-like lesions on fruit",
            "Defoliation and blossom drop in severe cases",
        ],
        "treatment": [
            "Apply copper hydroxide bactericides preventively",
            "Use disease-free certified seed and transplants",
            "Avoid overhead irrigation",
            "Remove infected plant debris from field",
        ],
        "prevention": "Do not transplant into fields with history of bacterial spot.",
    },
    "Tomato___Early_blight": {
        "plant": "Tomato",
        "disease": "Early Blight",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Early blight is caused by Alternaria solani. "
            "It typically affects older leaves first and moves upward."
        ),
        "symptoms": [
            "Brown lesions with concentric rings forming a target pattern",
            "Yellow halo surrounding lesions",
            "Premature defoliation from lower leaves upward",
            "Sunken, dark lesions with target pattern on fruit",
        ],
        "treatment": [
            "Apply chlorothalonil, mancozeb, or copper fungicides",
            "Remove infected lower leaves",
            "Avoid excessive nitrogen fertilization",
            "Stake plants to improve air circulation",
        ],
        "prevention": "Use mulch to prevent soil splash; maintain adequate plant spacing.",
    },
    "Tomato___Late_blight": {
        "plant": "Tomato",
        "disease": "Late Blight",
        "healthy": False,
        "severity": "Critical",
        "description": (
            "Late blight is caused by Phytophthora infestans. "
            "It can destroy an entire crop in days under favorable conditions."
        ),
        "symptoms": [
            "Large, water-soaked gray-green lesions on leaves",
            "White fuzzy growth on underside of leaves",
            "Brown-black firm lesions on stems",
            "Large, brown, greasy lesions on fruit",
        ],
        "treatment": [
            "Apply metalaxyl, cymoxanil, or chlorothalonil fungicides immediately",
            "Destroy infected plants — do not compost",
            "Harvest fruit before infection spreads to fruit",
        ],
        "prevention": "Avoid overhead irrigation; plant resistant varieties.",
    },
    "Tomato___Leaf_Mold": {
        "plant": "Tomato",
        "disease": "Leaf Mold",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Leaf mold is caused by Passalora fulva (formerly Fulvia fulva). "
            "It is most common in greenhouse-grown tomatoes."
        ),
        "symptoms": [
            "Pale green to yellow spots on upper leaf surface",
            "Olive-green to gray-brown velvety mold on leaf underside",
            "Infected leaves curl upward and eventually die",
            "Rarely affects fruit but reduces yield",
        ],
        "treatment": [
            "Improve greenhouse ventilation to reduce humidity below 85%",
            "Apply fungicides (chlorothalonil, copper) preventively",
            "Remove and destroy infected leaves",
            "Avoid working with wet plants",
        ],
        "prevention": "Maintain relative humidity below 85%; space plants adequately.",
    },
    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato",
        "disease": "Septoria Leaf Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Septoria leaf spot is caused by Septoria lycopersici. "
            "It is one of the most destructive diseases of tomato foliage."
        ),
        "symptoms": [
            "Numerous small circular spots with dark borders and gray-white centers",
            "Tiny black dots (pycnidia) in the center of lesions",
            "Severe defoliation starting from lower leaves",
            "Fruit not directly affected but indirect yield loss from defoliation",
        ],
        "treatment": [
            "Apply chlorothalonil, mancozeb, or copper fungicides",
            "Remove infected leaves promptly",
            "Avoid overhead irrigation",
            "Mulch around plants to prevent soil splash",
        ],
        "prevention": "Practice 2–3 year crop rotation with non-solanaceous crops.",
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato",
        "disease": "Spider Mites (Two-Spotted Spider Mite)",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Two-spotted spider mite (Tetranychus urticae) is a major pest of tomatoes, "
            "especially in hot, dry conditions."
        ),
        "symptoms": [
            "Yellowing, stippling (tiny dots) on upper leaf surface",
            "Fine webbing on underside of leaves",
            "Bronzing and drying of heavily infested leaves",
            "Severe infestations cause complete defoliation",
        ],
        "treatment": [
            "Apply miticides (abamectin, bifenazate) for severe infestations",
            "Use insecticidal soap or neem oil for mild infestations",
            "Introduce predatory mites (Phytoseiulus persimilis) for biological control",
            "Spray plants with strong jets of water to dislodge mites",
        ],
        "prevention": "Avoid over-fertilization with nitrogen; maintain adequate humidity.",
    },
    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "disease": "Target Spot",
        "healthy": False,
        "severity": "Moderate",
        "description": (
            "Target spot is caused by Corynespora cassiicola. "
            "It is increasingly common in tomato-growing regions worldwide."
        ),
        "symptoms": [
            "Brown lesions with concentric rings (target pattern) on leaves",
            "Lesions may have yellow halos",
            "Defoliation of lower leaves",
            "Sunken, dark brown lesions with rings on fruit",
        ],
        "treatment": [
            "Apply azoxystrobin, chlorothalonil, or mancozeb fungicides",
            "Remove infected plant material",
            "Improve air circulation through staking and pruning",
        ],
        "prevention": "Avoid dense planting; use mulch to reduce soil splash.",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "healthy": False,
        "severity": "Critical",
        "description": (
            "TYLCV is a devastating viral disease transmitted by the silverleaf whitefly "
            "(Bemisia tabaci). It has no cure and can cause complete crop loss."
        ),
        "symptoms": [
            "Severe upward leaf curling and cupping",
            "Yellowing of leaf margins and interveinal areas",
            "Stunted plant growth",
            "Reduced flower set and fruit production",
        ],
        "treatment": [
            "No cure — remove and destroy infected plants immediately",
            "Control whitefly vectors with insecticides (imidacloprid) or yellow sticky traps",
            "Use reflective mulches to repel whiteflies",
            "Plant TYLCV-resistant tomato varieties",
        ],
        "prevention": "Use insect-proof netting in greenhouse production; inspect transplants carefully.",
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "healthy": False,
        "severity": "High",
        "description": (
            "Tomato mosaic virus is a highly stable virus transmitted mechanically "
            "through contact with infected plants, tools, and soil."
        ),
        "symptoms": [
            "Light and dark green mosaic mottling pattern on leaves",
            "Leaf distortion, curling, and fern-like appearance",
            "Stunted plant growth",
            "Fruit may show yellow blotches or internal browning",
        ],
        "treatment": [
            "No chemical cure — remove infected plants",
            "Disinfect tools with 10% bleach or 70% alcohol between uses",
            "Wash hands thoroughly before handling plants",
            "Plant resistant tomato varieties (ToMV-resistant)",
        ],
        "prevention": "Do not use tobacco products near tomato plants; ToMV can be on tobacco.",
    },
    "Tomato___healthy": {
        "plant": "Tomato",
        "disease": "Healthy",
        "healthy": True,
        "severity": "None",
        "description": "This tomato leaf appears healthy with no signs of disease or pest damage.",
        "symptoms": [],
        "treatment": [],
        "prevention": "Maintain proper watering, staking, and regular scouting for pests and diseases.",
    },
}


def get_disease_info(class_name: str) -> dict:
    """
    Returns disease information for a given class name.
    Falls back to a generic response if class not found.
    """
    return DISEASE_INFO.get(class_name, {
        "plant": "Unknown",
        "disease": "Unknown",
        "healthy": False,
        "severity": "Unknown",
        "description": "No information available for this class.",
        "symptoms": [],
        "treatment": ["Consult an agricultural expert for diagnosis and treatment."],
        "prevention": "Monitor crops regularly and consult local agricultural extension services.",
    })


def get_severity_color(severity: str) -> str:
    """Returns a CSS color class based on severity level."""
    return {
        "None": "severity-healthy",
        "Moderate": "severity-moderate",
        "High": "severity-high",
        "Critical": "severity-critical",
    }.get(severity, "severity-unknown")
