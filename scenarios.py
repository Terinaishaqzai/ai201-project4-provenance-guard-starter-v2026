"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of my five criteria (criteria.md) and what tests it:

  Criterion 1  False positives      -> scenario "my own writing" (10 pieces I wrote)
  Criterion 2  Score separation     -> "my own writing" (human half) + "ai samples" (AI half)
  Criterion 3  Label coverage       -> eval_extra.py (calls scoring.score_to_label directly;
                                       it is a property of the label mapping, not of any text)
  Criterion 4  Appeal handling      -> eval_extra.py (needs submit -> content_id -> appeal,
                                       which a texts/bodies scenario cannot express)
  Criterion 5  Invalid inputs       -> scenario "invalid inputs" (4 bodies) + eval_extra.py
                                       (the 5th case, a JSON body that is not an object,
                                       can't be written as a dict here)

`run_eval.py` runs everything in SCENARIOS three times.
`eval_extra.py` runs criteria 3, 4 and the 5th case of criterion 5 three times.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Ten pieces from my own essay, "A World Connected: The Historical Process of
        # Globalization from 1000 CE to Today" (written without AI). Split by paragraph;
        # the three longest paragraphs are split in two. Title and Works Cited excluded.
        # Also the human half of criterion 2.
        "texts": [
            "From the camel caravans of the medieval Silk Roads to the fiber optic cables of the modern internet, globalization has been a continuous yet transforming process. Between 1000 CE and today, it advanced through four overlapping mechanisms: the expansion of long distance trade networks, the coercive reach of imperial power, the integrating shock of global conflict, and the accelerating force of technological innovation. In each era, these mechanisms deepened the world's interconnectedness while simultaneously entrenching inequalities between the nations and peoples who profited from global exchange and those who were exploited by it. Tracing this process from medieval Afro Eurasia through the trans Atlantic slave trade, nineteenth century imperialism, two world wars, the Cold War, and into the digital age reveals that globalization has never been a neutral phenomenon: it has always reflected and reinforced existing structures of power.",
            'The earliest phase of globalization between 1000 and 1400 CE was built on the integrated trade and cultural networks of Afro Eurasia. Overland routes known collectively as the Silk Roads carried silk, spices, porcelain, and cotton textiles from China and India westward to the Middle East, Africa, and Europe, connecting distant economies through mutual demand for luxury goods (Liu, The Silk Roads). The Chinese chronicler Zhao Rukuo described the port city of Guangzhou as a hub where merchants from across the known world exchanged commodities evidence of how thoroughly economic interdependence had taken hold (Zhao Rukuo, Records Concerning Foreign Countries). The Indian Ocean system functioned similarly, with Muslim merchants exploiting predictable monsoon winds to link Arabia, India, and East Africa. Along these same corridors, Buddhism spread through Central Asia, Islam expanded across sub Saharan Africa, and the Black Death swept from Asia to Europe in the fourteenth century an unintended but powerful demonstration of how connected the world had already become (Wiesner-Hanks et al. 312-315).',
            'By the seventeenth and eighteenth centuries, globalization expanded dramatically in both geographic scope and coercive character. The trans Atlantic trade permanently integrated the Americas into global networks, creating a triangular system linking Europe, Africa, and the New World. European manufactured goods were exchanged in West Africa for enslaved people, who were transported across the Atlantic to produce sugar, tobacco, and cotton on plantation colonies in the Caribbean and Brazil. These commodities generated enormous profits and transformed European society; sugar reshaped diets, and coffeehouses became centers of commercial life. The primary source The Journey to Slavery illustrates the immense human suffering on which this global economy rested suffering that was foundational, not incidental, to its functioning (Strayer and Nelson, Thinking Through Sources, pp. 211-214). Simultaneously, joint stock companies like the British East India Company used royal charters, monopoly rights, and military force to subordinate Indian Ocean trade networks to European imperial interests, shifting the basin from a relatively balanced commercial system toward one of European dominance (Strayer and Nelson, Ways of the World, pp. 600-603).',
            'During the nineteenth century, industrialization gave Western nations unprecedented advantages that they used to reshape the global order through imperialism. The Industrial Revolution created insatiable demand for raw materials rubber, palm oil, cotton, metals drawing Africa and Asia ever more tightly into a world economy structured to serve European manufacturing. The Berlin Conference of 1884 - 1885 formalized this arrangement: European powers divided Africa among themselves through diplomacy, without any African representation, institutionalizing imperial dominance over an entire continent (Wiesner-Hanks et al. 712 - 715).',
            'In the Congo Free State, local populations were coerced through violence and the threat of death into meeting rubber quotas that fed European industries, as documented in oral testimonies from the region (Grant, The Congo Free State and the New Imperialism, Document 12). The pattern was consistent across colonized territories: raw materials flowed outward to industrialized centers while colonized peoples were integrated into global commerce primarily as laborers. This asymmetry would define global economic relationships well into the twentieth century.',
            'The two World Wars simultaneously devastated and deepened global interconnectedness. World War I drew colonial subjects from Africa, Asia, and the Caribbean into a European conflict, demonstrating the inescapable reach of imperial networks (Wiesner-Hanks et al. 756-758). World War II fused two regional conflicts into a single global struggle; by 1942, virtually every corner of the earth had been touched by the fighting. After 1945, institutions like the United Nations and the World Bank were founded to manage global interdependence through multilateral cooperation. The Great Depression had already shown how deeply national economies were intertwined: financial collapse in the United States had destabilized governments across the world and fueled the authoritarian regimes whose aggression produced the war (Wiesner-Hanks et al. 810-812).',
            "The Cold War then extended integration through superpower competition. The Marshall Plan rebuilt Western European economies as trading partners for American goods, while President Truman's 1947 Doctrine pledged American support to nations resisting communist expansion entangling the United States in the internal affairs of countries from Greece to Korea (Truman, Truman Doctrine, 1947). The Cuban Missile Crisis of 1962 made clear just how globally consequential superpower rivalry had become (Kennedy, Radio and Television Report, 1962).",
            'Between 1950 and 2000, technology and transnational corporations became the twin engines of an accelerating globalization. Early mainframe computers evolved into personal computers by the 1980s, and by the 1990s the internet connected millions worldwide, collapsing the time and distance that had always defined the limits of human exchange. Businesses could coordinate production across continents in real time, and corporations like Nike, Coca Cola, Toyota, and Samsung built supply chains spanning dozens of countries (Strayer and Nelson, Ways of the World, p. 971).',
            'This model of global corporate organization extended a pattern established by the joint stock companies of the seventeenth century and the imperial resource extraction of the nineteenth. Yet the inequalities of those earlier eras persisted: developing nations continued to supply raw materials and cheap labor without fully sharing in the profits generated, widening the gap between wealthy industrialized nations and the rest of the world (Strayer and Nelson, Ways of the World, p. 971). The digital revolution had made the world smaller without making it more equal.',
            "From the Silk Roads to the smartphone, globalization from 1000 CE to today has been driven by four interlocking forces: trade, imperial power, conflict, and technology. Each era intensified the world's interconnectedness, and each era reproduced the inequality that has always accompanied it. Today, that pattern continues: global supply chains fractured by a pandemic, social media platforms connecting billions while spreading misinformation across borders, and climate change demanding international cooperation that the structures of sovereign nation states were never designed to provide. The world is more integrated than at any point in history and the question of who bears the costs of that integration, as in every century before, remains urgently unresolved.",
        ],
    },
    {
        "name": "ai samples",
        "criterion": 2,
        # Ten AI-generated paragraphs (written by Claude for this test, unedited).
        # The AI half of criterion 2.
        "texts": [
            "Effective time management is an essential skill for students and professionals alike. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can significantly improve their productivity. One useful strategy is to break larger projects into smaller, more manageable steps. This approach reduces feelings of overwhelm and makes it easier to track progress. Additionally, scheduling regular breaks can help maintain focus and prevent burnout. Ultimately, developing strong time management habits leads to better outcomes and a healthier work-life balance.",
            "Climate change represents one of the most pressing challenges facing our world today. Rising global temperatures are contributing to more frequent extreme weather events, rising sea levels, and disruptions to ecosystems. Addressing this issue requires a combination of individual action, corporate responsibility, and government policy. Transitioning to renewable energy sources, improving energy efficiency, and protecting natural habitats are all important steps. By working together, communities around the world can reduce emissions and build a more sustainable future for generations to come.",
            "Regular physical activity offers numerous benefits for both physical and mental health. Exercise strengthens the heart, improves circulation, and helps maintain a healthy weight. It also plays a key role in reducing stress and improving mood by releasing endorphins. Experts generally recommend at least 150 minutes of moderate activity each week. Activities such as walking, swimming, and cycling are accessible options for people of all fitness levels. Incorporating movement into daily routines can lead to lasting improvements in overall well-being.",
            "Artificial intelligence is transforming the way businesses operate across a wide range of industries. From automating routine tasks to analyzing large datasets, AI tools can help organizations make faster and more informed decisions. However, the adoption of AI also raises important ethical considerations, including concerns about privacy, bias, and job displacement. It is essential for companies to implement AI responsibly and transparently. By balancing innovation with accountability, organizations can harness the benefits of AI while minimizing potential risks.",
            "Reading regularly provides a wide range of cognitive and personal benefits. It expands vocabulary, improves concentration, and enhances critical thinking skills. Fiction in particular can help readers develop empathy by allowing them to see the world through different perspectives. Nonfiction, on the other hand, offers opportunities to learn about new topics and ideas. Setting aside even a small amount of time each day for reading can make a meaningful difference. Over time, this habit can contribute to lifelong learning and personal growth.",
            "Effective communication is a cornerstone of successful teamwork. When team members share information clearly and openly, they are better able to coordinate their efforts and achieve common goals. Active listening is an important part of this process, as it ensures that everyone feels heard and understood. Providing constructive feedback and addressing conflicts early can also strengthen working relationships. By fostering a culture of open communication, teams can improve collaboration, increase productivity, and create a more positive work environment.",
            "The rise of remote work has fundamentally changed the modern workplace. Many employees now enjoy greater flexibility, reduced commuting time, and an improved work-life balance. At the same time, remote work presents challenges such as feelings of isolation and difficulties with collaboration. To address these issues, organizations are adopting new tools and practices, including video conferencing and virtual team-building activities. As technology continues to evolve, hybrid work models are likely to remain an important part of the professional landscape.",
            "Financial literacy is an important skill that empowers individuals to make informed decisions about their money. Understanding concepts such as budgeting, saving, and investing can help people achieve their financial goals and avoid unnecessary debt. Creating a monthly budget is a practical first step toward gaining control over personal finances. It is also wise to build an emergency fund to cover unexpected expenses. By developing strong financial habits early, individuals can build a more secure and stable future.",
            "Sleep plays a vital role in maintaining overall health and well-being. During sleep, the body repairs tissues, consolidates memories, and regulates important hormones. Most adults need between seven and nine hours of sleep each night to function at their best. Poor sleep has been linked to a variety of health issues, including weakened immunity and difficulty concentrating. Establishing a consistent sleep schedule and limiting screen time before bed can help improve sleep quality and support better daily performance.",
            "Volunteering is a meaningful way to give back to the community while also gaining valuable experience. By donating their time and skills, volunteers can support important causes and make a positive impact on the lives of others. Volunteering also offers personal benefits, such as developing new skills, expanding social networks, and increasing a sense of purpose. Many organizations offer flexible opportunities that fit a variety of schedules. Ultimately, volunteering helps build stronger, more connected communities.",
        ],
    },
    {
        "name": "invalid inputs",
        "criterion": 5,
        # Four of the five invalid cases. The fifth (a JSON body that is not an
        # object) is sent by eval_extra.py, because a body here must be a dict.
        "bodies": [
            {"creator_id": "eval_bad_missing_text"},                  # missing text
            {"text": "", "creator_id": "eval_bad_empty_text"},        # empty text
            {"text": "     \n\t  ", "creator_id": "eval_bad_whitespace"},  # whitespace only
            {"text": "This request has text but no creator id at all, so it should be refused."},  # missing creator_id
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems