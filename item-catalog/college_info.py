from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from college_database import College, Base, Branch, User
engine = create_engine('sqlite:///collegedata.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

User1 = User(
    name="Pavan Kumar966647",
    email="pavankumar285765@gmail.com",
    picture="https://lh3.googleusercontent.com/"
            "a-/AAuE7mC8im3YRLZRdKOXHlbafo85SfzotOcn2Yxj2xs9cQ=s192")
session.add(User1)
session.commit()

college1 = College(name="VIT", user_id=1)
session.add(college1)
session.commit()

branch1 = Branch(
    branch_name="Computer Science and Engineering",
    about="Department is committed to offering a stimulating program"
          "with strong emphasis on high quality, state of the art"
          "education and research in the highly diverse and "
          "cosmopolitan environment.",
    class_strength="180",
    labs="5",
    faculties="33",
    block="A-Block 2nd floar",
    branch_id=1,
    user_id=1
    )
session.add(branch1)
session.commit()

branch2 = Branch(
    branch_name="Electronics & Communication Engineering",
    about="All of the applications which make our life easier"
          "and enjoyable such as Television, Radio, Computers, Mobiles etc."
          "are designed and developed by Electronics and"
          "Communication Engineers.",
    class_strength="180",
    labs="9",
    faculties="41",
    block="A-Block 1st floar",
    branch_id=1,
    user_id=1
    )
session.add(branch2)
session.commit()

branch3 = Branch(
    branch_name="Electrical Electronics Engineering",
    about="The branch of engineering that deals with the technology"
          "of electricity. Electrical engineers work on a wide range"
          "of components, devices and systems, from tiny microchips"
          "to huge power station generators.",
    class_strength="110",
    labs="8",
    faculties="32",
    block="A-Block ground floar",
    branch_id=1,
    user_id=1
    )
session.add(branch3)
session.commit()

branch4 = Branch(
    branch_name="Mechanical Engineering",
    about="The goal of the Mechanical Engineering department"
          "is to provide students with a balance of intellectual"
          "and practical experiences that enable them to address "
          "a variety of societal needs and also aligns academic"
          "course work with research to prepare scholars in "
          "specialized areas within the field.",
    class_strength="120",
    labs="14",
    faculties="29",
    block="B-Block 1st floar",
    branch_id=1,
    user_id=1
    )
session.add(branch4)
session.commit()

branch5 = Branch(
    branch_name="Information Technology",
    about="help you add value to your career by adding to "
          "your existing knowledge with important foundational "
          "skills. In addition to technological competency, "
          "communication and organizational skills can help "
          "set you apart.",
    class_strength="60",
    labs="5",
    faculties="32",
    block="B-Block ground floar",
    branch_id=1,
    user_id=1
    )
session.add(branch5)
session.commit()

branch6 = Branch(
    branch_name="Civil Engineering",
    about="Civil Engineering Students are not only made experts"
          "in technical aspects but also in interpersonal skills,"
          "a vital ingredient to excel in the fast-paced world.",
    class_strength="60",
    labs="6",
    faculties="30",
    block="B-Block 1st floar",
    branch_id=1,
    user_id=1
    )
session.add(branch6)
session.commit()

college2 = College(name="Svecw", user_id=1)
session.add(college2)
session.commit()

branch1 = Branch(
    branch_name="Computer Science & Engineering",
    about="Department is committed to offering a stimulating"
          "program with strong emphasis on high quality, state"
          "of the art education and research in the highly"
          "diverse and cosmopolitan environment.",
    class_strength="290",
    labs="12",
    faculties="62",
    block="A-Block",
    branch_id=2,
    user_id=1
    )
session.add(branch1)
session.commit()

branch2 = Branch(
    branch_name="Electronics & Communication Engineering",
    about="All of the applications which make our life easier"
          "and enjoyable such as Television, Radio, Computers,"
          "Mobiles etc. are designed and developed by Electronics"
          "and Communication Engineers.",
    class_strength="310",
    labs="16",
    faculties="61",
    block="C-Block",
    branch_id=2,
    user_id=1
    )
session.add(branch2)
session.commit()

branch3 = Branch(
    branch_name="Electrical Electronics Engineering",
    about="The branch of engineering that deals with the technology"
          "of electricity. Electrical engineers work on a wide range"
          "of components, devices and systems, from tiny microchips"
          "to huge power station generators.",
    class_strength="260",
    labs="18",
    faculties="52",
    block="B-Block",
    branch_id=2,
    user_id=1
    )
session.add(branch3)
session.commit()

branch4 = Branch(
    branch_name="Mechanical Engineering",
    about="The goal of the Mechanical Engineering department"
          "is to provide students with a balance of intellectual"
          "and practical experiences that enable them to address"
          "a variety of societal needs and also aligns academic"
          "course work with research to prepare scholars in"
          "specialized areas within the field.",
    class_strength="220",
    labs="14",
    faculties="39",
    block="D-Block",
    branch_id=2,
    user_id=1
    )
session.add(branch4)
session.commit()

branch5 = Branch(
    branch_name="Information Technology",
    about="help you add value to your career by adding to your"
          "existing knowledge with important foundational skills."
          "In addition to technological competency, communication"
          "and organizational skills can help set you apart.",
    class_strength="160",
    labs="8",
    faculties="26",
    block="A-Block",
    branch_id=2,
    user_id=1
    )
session.add(branch5)
session.commit()

branch6 = Branch(
    branch_name="Civil Engineering",
    about="Civil Engineering Students are not only made expert"
          "s in technical aspects but also in interpersonal skills, "
          "a vital ingredient to excel in the fast-paced world.",
    class_strength="190",
    labs="16",
    faculties="36",
    block="D-Block",
    branch_id=2,
    user_id=1
    )
session.add(branch6)
session.commit()

college3 = College(name="Dental", user_id=1)
session.add(college3)
session.commit()

branch1 = Branch(
    branch_name="Oral Medicine & Radiology",
    about="Mouth is a mirror of systemic disease; It is the oral"
          "medicine specialist who addresses these situations where"
          "a systemic disease is connected with typical oral manifestations.",
    class_strength="120",
    labs="6",
    faculties=16,
    block="Dental A-Block",
    branch_id=3,
    user_id=1
    )

session.add(branch1)
session.commit()

branch2 = Branch(
    branch_name="Periodontology and Implantology",
    about="Department of Periodontology and Implantology is located"
          "in the ground floor of the IInd block of Vishnu dental college."
          "It stands over an area of 3734sft with separate undergraduate"
          "and post graduate sections.",
    class_strength="100",
    labs="4",
    faculties=12,
    block="Dental A-Block",
    branch_id=3,
    user_id=1
    )
session.add(branch2)
session.commit()

branch3 = Branch(
    branch_name="Dental Meterials",
    about="Dental Materials Science is an interdisciplinary area"
          "that applies biology, chemistry, and physics to the development,"
          "understanding, and evaluation of materials used in the"
          "practice of dentistry.",
    class_strength="90",
    labs="2",
    faculties=10,
    block="Dental B-Block",
    branch_id=3,
    user_id=1
    )
session.add(branch3)
session.commit()

branch4 = Branch(
    branch_name="Conservative Dentistry and Endodontics",
    about="Conservative Dentistry and Endodontics is the branch "
          "of dentistry which deals with the treatment of caries,"
          "malformed, discolored, unesthetic, or fractured teeth"
          "and Endodontics deals with treatment of pulpal and "
          "periapical diseases and dental pain management.",
    class_strength="180",
    labs="8",
    faculties=19,
    block="Dental C-Block",
    branch_id=3,
    user_id=1
    )
session.add(branch4)
session.commit()

branch5 = Branch(
    branch_name="Orthodontics",
    about="Orthodontics is the branch of Science and the art of"
          "dentistry which deals with the development and anomalies"
          "of the teeth and the jaws that affect oral health, esthetic"
          "and mental well being of the person.",
    class_strength="200",
    labs="3",
    faculties=14,
    block="Dental B-Block",
    branch_id=3,
    user_id=1
    )
session.add(branch5)
session.commit()


college4 = College(name="Pharmacy", user_id=1)
session.add(college4)
session.commit()

branch1 = Branch(
    branch_name="B.Pharmacy",
    about="Pharmacy as an academic discipline provides exemplary"
          "education in a stimulating environment where delivery "
          "of pharmaceutical knowledge is integrated with multidisciplinary,"
          "multifaceted curriculum and cutting-edge research in the discovery,"
          "development, utilization and evaluation of therapeutic agents.",
    class_strength="250",
    labs="9",
    faculties=18,
    block="ground floar",
    branch_id=4,
    user_id=1
    )

session.add(branch1)
session.commit()

branch2 = Branch(
    branch_name="M.Pharmacy",
    about="Pharmacy as an academic discipline provides exemplary "
          "education in a stimulating environment where delivery "
          "of pharmaceutical knowledge is integrated with multidisciplinary,"
          "multifaceted curriculum and cutting-edge research in the discovery,"
          "development, utilization and evaluation of therapeutic agents.",
    class_strength="220",
    labs="6",
    faculties=18,
    block="1st floar",
    branch_id=4,
    user_id=1
    )

session.add(branch2)
session.commit()

branch3 = Branch(
    branch_name="M.Pharmacy",
    about="An establishment of better healthcare system is one of the"
          "primary objectives of a nation to build a healthy society"
          "for better future. The healthcare system has to develop"
          "patient centred treatment approach that is supported by "
          "doctors, pharmacists, nurses etc.",
    class_strength="190",
    labs="12",
    faculties=16,
    block="D.P ground floar",
    branch_id=4,
    user_id=1
    )

session.add(branch3)
session.commit()


college5 = College(name="Degree", user_id=1)
session.add(college5)
session.commit()

branch1 = Branch(
    branch_name="Computer Science",
    about="Department is committed to offering a stimulating program"
          "with strong emphasis on high quality, state of the art "
          "education and research in the highly diverse and "
          "cosmopolitan environment.",
    class_strength="250",
    labs="5",
    faculties=13,
    block="ground floar",
    branch_id=5,
    user_id=1
    )

session.add(branch1)
session.commit()

branch2 = Branch(
    branch_name="Chemistry",
    about="The department is supported by qualified and experienced"
          "faculty who impart required guidance to students in their"
          "curriculum, projects and placements along with intellectual "
          "and psychological bolstering.",
    class_strength="220",
    labs="3",
    faculties=7,
    block="1st floar",
    branch_id=5,
    user_id=1
    )

session.add(branch2)
session.commit()

branch3 = Branch(
    branch_name="Commerce",
    about="This course bridges the gap between the commerce and "
          "computers discipline. The course aims at comprehensive "
          "development of students in the field of Business and Industry.",
    class_strength="110",
    labs="0",
    faculties=6,
    block="1st floar",
    branch_id=5,
    user_id=1
    )

session.add(branch3)
session.commit()

branch4 = Branch(
    branch_name="Life Science",
    about="it offers two streams of Biotechnology, one with Biotechnology,"
          "Biochemistry and Microbiology and the other with Biotechnology, "
          "Biochemistry and Chemistry. Students are not only made experts"
          "in practical aspects but also in interpersonal skills, a vital"
          "ingredient to excel in the fast-paced world.",
    class_strength="130",
    labs="4",
    faculties=10,
    block="2nd floar",
    branch_id=5,
    user_id=1
    )

session.add(branch4)
session.commit()
print("List of branches are added")
