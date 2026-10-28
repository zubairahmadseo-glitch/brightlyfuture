"""Verified sources (PubMed IDs checked against the abstract on 2026-10-28)."""

PM = "https://pubmed.ncbi.nlm.nih.gov/"

R = {
    "acsm2026": ("Currier BS, et al. American College of Sports Medicine Position Stand: Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults. <em>Med Sci Sports Exerc</em>. 2026.", PM + "41843416/"),
    "acsm2009": ("American College of Sports Medicine. Position stand: Progression models in resistance training for healthy adults. <em>Med Sci Sports Exerc</em>. 2009.", PM + "19204579/"),
    "freq2016": ("Schoenfeld BJ, Ogborn D, Krieger JW. Effects of resistance training frequency on measures of muscle hypertrophy: a systematic review and meta-analysis. <em>Sports Med</em>. 2016.", PM + "27102172/"),
    "vol2017": ("Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass. <em>J Sports Sci</em>. 2017.", PM + "27433992/"),
    "vol2019": ("Schoenfeld BJ, et al. Resistance training volume enhances muscle hypertrophy but not strength in trained men. <em>Med Sci Sports Exerc</em>. 2019.", PM + "30153194/"),
    "pelland2026": ("Pelland JC, et al. The resistance training dose response: meta-regressions exploring the effects of weekly volume and frequency on muscle hypertrophy and strength gains. <em>Sports Med</em>. 2026.", PM + "41343037/"),
    "split2024": ("Ramos-Campo DJ, et al. Efficacy of split versus full-body resistance training on strength and muscle growth: a systematic review with meta-analysis. <em>J Strength Cond Res</em>. 2024.", PM + "38595233/"),
    "split2015": ("Schoenfeld BJ, et al. Influence of resistance training frequency on muscular adaptations in well-trained men. <em>J Strength Cond Res</em>. 2015.", PM + "25932981/"),
    "rest2016": ("Schoenfeld BJ, et al. Longer interset rest periods enhance muscle strength and hypertrophy in resistance-trained men. <em>J Strength Cond Res</em>. 2016.", PM + "26605807/"),
    "rest2018": ("Grgic J, et al. Effects of rest interval duration in resistance training on measures of muscular strength: a systematic review. <em>Sports Med</em>. 2018.", PM + "28933024/"),
    "failure2023": ("Refalo MC, et al. Influence of resistance training proximity-to-failure on skeletal muscle hypertrophy: a systematic review with meta-analysis. <em>Sports Med</em>. 2023.", PM + "36334240/"),
    "load2021": ("Lopez P, et al. Resistance training load effects on muscle hypertrophy and strength gain: systematic review and network meta-analysis. <em>Med Sci Sports Exerc</em>. 2021.", PM + "33433148/"),
    "currier2023": ("Currier BS, et al. Resistance training prescription for muscle strength and hypertrophy in healthy adults: a systematic review and Bayesian network meta-analysis. <em>Br J Sports Med</em>. 2023.", PM + "37414459/"),
    "freqstr2018": ("Grgic J, et al. Effect of resistance training frequency on gains in muscular strength: a systematic review and meta-analysis. <em>Sports Med</em>. 2018.", PM + "29470825/"),
    "delphi2023": ("Bell L, et al. Integrating deloading into strength and physique sports training programmes: an international Delphi consensus approach. <em>Sports Med Open</em>. 2023.", PM + "37730925/"),
    "deload2024": ("Rogerson D, et al. Deloading practices in strength and physique sports: a cross-sectional survey. <em>Sports Med Open</em>. 2024.", PM + "38499934/"),
    "protein2018": ("Morton RW, et al. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength. <em>Br J Sports Med</em>. 2018.", PM + "28698222/"),
    "issnprotein": ("Jäger R, et al. International Society of Sports Nutrition position stand: protein and exercise. <em>J Int Soc Sports Nutr</em>. 2017.", PM + "28642676/"),
    "offseason2019": ("Iraki J, et al. Nutrition recommendations for bodybuilders in the off-season: a narrative review. <em>Sports (Basel)</em>. 2019.", PM + "31247944/"),
    "surplus2019": ("Slater GJ, et al. Is an energy surplus required to maximize skeletal muscle hypertrophy associated with resistance training? <em>Front Nutr</em>. 2019.", PM + "31482093/"),
    "garthe2013": ("Garthe I, et al. Effect of nutritional intervention on body composition and performance in elite athletes. <em>Eur J Sport Sci</em>. 2013.", PM + "23679146/"),
    "creatine": ("Kreider RB, et al. International Society of Sports Nutrition position stand: safety and efficacy of creatine supplementation in exercise, sport, and medicine. <em>J Int Soc Sports Nutr</em>. 2017.", PM + "28615996/"),
    "sex2020": ("Roberts BM, Nuckols G, Krieger JW. Sex differences in resistance training: a systematic review and meta-analysis. <em>J Strength Cond Res</em>. 2020.", PM + "32218059/"),
    "hubal2005": ("Hubal MJ, et al. Variability in muscle size and strength gain after unilateral resistance training. <em>Med Sci Sports Exerc</em>. 2005.", PM + "15947721/"),
    "cycle2023": ("Colenso-Semple LM, et al. Current evidence shows no influence of women's menstrual cycle phase on acute strength performance or adaptations to resistance exercise training. <em>Front Sports Act Living</em>. 2023.", PM + "37033884/"),
    "liftmor2018": ("Watson SL, et al. High-intensity resistance and impact training improves bone mineral density and physical function in postmenopausal women with osteopenia and osteoporosis: the LIFTMOR randomized controlled trial. <em>J Bone Miner Res</em>. 2018.", PM + "28975661/"),
    "rpe2016": ("Zourdos MC, et al. Novel resistance training-specific rating of perceived exertion scale measuring repetitions in reserve. <em>J Strength Cond Res</em>. 2016.", PM + "26049792/"),
    "taper2020": ("Travis SK, et al. Tapering and peaking maximal strength for powerlifting performance: a review. <em>Sports (Basel)</em>. 2020.", PM + "32917000/"),
    "kraemer2004": ("Kraemer WJ, Ratamess NA. Fundamentals of resistance training: progression and exercise prescription. <em>Med Sci Sports Exerc</em>. 2004.", PM + "15064596/"),
    "maeo2021": ("Maeo S, et al. Greater hamstrings muscle hypertrophy but similar damage protection after training at long versus short muscle lengths. <em>Med Sci Sports Exerc</em>. 2021.", PM + "33009197/"),
    "restsys2017": ("Grgic J, et al. The effects of short versus long inter-set rest intervals in resistance training on measures of muscle hypertrophy: a systematic review. <em>Eur J Sport Sci</em>. 2017.", PM + "28641044/"),
    "wolf2025": ("Wolf M, et al. Lengthened partial repetitions elicit similar muscular adaptations as full range of motion repetitions during resistance training in trained individuals. <em>PeerJ</em>. 2025.", PM + "39959841/"),
    "dropset2026": ("Havers T, et al. Acute and chronic effects of drop-set training: a meta-analysis and systematic review. <em>Sports Med Open</em>. 2026.", PM + "41920484/"),
    "advanced2026": ("Tsartsapakis I, et al. Effects of advanced resistance training systems on muscle hypertrophy and strength in recreationally trained adults: a systematic review and meta-analysis. <em>J Funct Morphol Kinesiol</em>. 2026.", PM + "41718208/"),
    "radaelli2015": ("Radaelli R, et al. Dose-response of 1, 3, and 5 sets of resistance exercise on strength, local muscular endurance, and hypertrophy. <em>J Strength Cond Res</em>. 2015.", PM + "25546444/"),
    "seynnes2007": ("Seynnes OR, de Boer M, Narici MV. Early skeletal muscle hypertrophy and architectural changes in response to high-intensity resistance training. <em>J Appl Physiol</em>. 2007.", PM + "17053104/"),
    "ralston2017": ("Ralston GW, et al. The effect of weekly set volume on strength gain: a meta-analysis. <em>Sports Med</em>. 2017.", PM + "28755103/"),
}


def refs(*keys):
    return [R[k] for k in keys]


def cite(key, text):
    """Inline citation link to the source."""
    return f'<a href="{R[key][1]}" rel="noopener" target="_blank">{text}</a>'
