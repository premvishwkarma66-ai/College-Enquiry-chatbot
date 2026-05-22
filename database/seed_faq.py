from core.db import get_db
conn = get_db()
cur = conn.cursor()
cur.executemany(
    """
    INSERT INTO faq (question, answer)
    VALUES (?, ?)
    """,
    [
(
    "Hi",
    "Hello! 😊 How can I help you today?"
),
(
    "Hello",
    "Hi there! 👋 Feel free to ask me anything about the college."
),
(
    "Hey",
    "Hey! 😄 What would you like to know?"
),
(
    "Good morning",
    "Good morning! ☀️ Hope you have a great day. How can I help you?"
),
(
    "Good afternoon",
    "Good afternoon! 😊 What can I help you with?"
),
(
    "Good evening",
    "Good evening! 🌆 Feel free to ask your questions."
),

# -------- HOW ARE YOU / SMALL TALK --------

(
    "How are you?",
    "I'm doing great 😄 Thanks for asking! How can I help you today?"
),
(
    "How is your day?",
    "My day is going well 😊 I'm here to help students like you."
),
(
    "What are you doing?",
    "I'm here to help you with college-related information 😊"
),
(
    "Are you busy?",
    "Not at all 😄 I'm always here to help you."
),

# -------- BOT IDENTITY --------

(
    "Who are you?",
    "I'm the College Enquiry Assistant 🤖 here to help you with information about the college."
),
(
    "What is your name?",
    "I'm your friendly College Enquiry Assistant 😊"
),
(
    "Are you a human?",
    "No 😄 I'm a chatbot, but I try my best to help you like a real friend."
),
(
    "Who created you?",
    "I was created to assist students by providing college-related information in a friendly way 😊"
),
(
    "What can you do?",
    "I can help you with courses, admissions, hostel, placements, campus life, and more!"
),

# -------- THANK YOU / GOODBYE --------

(
    "Thank you",
    "You're most welcome! 😊 Happy to help."
),
(
    "Thanks",
    "Anytime 😄 Let me know if you need anything else."
),
(
    "Bye",
    "Goodbye! 👋 All the best for your studies."
),
(
    "See you",
    "See you! 😊 Feel free to come back anytime."
),

        # ---------- CAMPUS TOUR / VISIT ----------
        (
            "About college",
            "Jai Hind College of Engineering (JCOE), Kuran, Pune, established in 2010, is a private engineering college under the Jaihind Comprehensive Educational Institute. It offers undergraduate and postgraduate engineering programs and focuses on technical education for rural development. The college is affiliated with Savitribai Phule Pune University (SPPU) and is NAAC accredited."
        ),
        (
            "Where is the college located?",
            "Jai Hind College of Engineering is located at Gat No. 441, Kuran, Taluka Junnar, Pune – 410511, Maharashtra, India, near Junnar–Narayangaon in Pune district."
        ),
        (
            "When was the college established?",
            "Jai Hind College of Engineering was established in the year 2010."
        ),
        (
            "Which university is the college affiliated with?",
            "Jai Hind College of Engineering is affiliated with Savitribai Phule Pune University (SPPU), Pune."
        ),
        (
            "Is the college NAAC accredited?",
            "Yes, Jai Hind College of Engineering (JCOE), Kuran is NAAC accredited."
        ),

        # -------- COURSES OFFERED --------
        (
            "What courses are offered?",
            "JCOE offers B.E. (Bachelor of Engineering) and M.E./M.Tech programs in Civil, Computer, Mechanical, Electronics & Telecommunication, and Artificial Intelligence & Data Science."
        ),
        (
            "What are the undergraduate courses and intake?",
            "Artificial Intelligence & Data Science (60–120), Computer Engineering (60–120), Civil Engineering (30–60), Mechanical Engineering (60–120), Electronics & Telecommunication Engineering (60), Automobile Engineering (60)."
        ),
        (
            "What postgraduate courses are available?",
            "M.E. (AI & Data Science – 12), M.E. (Civil – Structural Engineering – 12), M.E. (Design Engineering – Mechanical – 12), M.E. (E&TC – Signal Processing – 6), M.E. (E&TC – VLSI & Embedded Systems – 6)."
        ),
        (
            "What is the duration of courses?",
            "B.E./B.Tech: 4 years, M.E./M.Tech: 2 years, Diploma Engineering: 3 years, B.Pharm: 4 years, D.Pharm: 2 years."
        ),

        # -------- ELIGIBILITY --------
        (
            "What is the eligibility for B.E.?",
            "Candidates must pass 10+2 with Physics and Mathematics and one optional subject with at least 45% marks (40% for reserved categories). Admission is through MHT-CET or JEE Main."
        ),
        (
            "What is the eligibility for direct second year?",
            "Candidates must have completed a Diploma in Engineering with at least 75% marks along with JEE Main."
        ),
        (
            "What is the eligibility for M.E. or M.Tech?",
            "Candidates must have passed B.E./B.Tech in a relevant discipline with a valid GATE score."
        ),
        (
            "What pharmacy courses are available?",
            "Bachelor of Pharmacy (B.Pharm – 4 years) and Diploma in Pharmacy (D.Pharm – 2 years) are available."
        ),
        (
            "What is the eligibility for diploma courses?",
            "After 10th: Minimum 35% marks. After 12th: Physics and Mathematics with at least 45% marks (40% for reserved categories)."
        ),

        # -------- FACULTY & ADMISSION --------
        (
            "How is the faculty?",
            "Faculty members are qualified, knowledgeable, and supportive, providing strong theoretical and practical guidance along with guest lectures and industry exposure."
        ),
        (
            "What is the admission process?",
            "Check eligibility, register for CAP on DTE Maharashtra website, fill the online application, upload documents, attend CAP counseling, and confirm admission after seat allotment."
        ),
        (
            "Which entrance exams are required?",
            "For B.E.: MHT-CET or JEE Main. For M.E./M.Tech: GATE."
        ),
        (
            "Is management quota available?",
            "Yes, management quota seats are available. Students must contact the college directly for details."
        ),

        # -------- FACILITIES --------
        (
            "Is hostel facility available?",
            "Yes, separate hostels for boys and girls are available with Wi-Fi, 24/7 water and electricity, security, gym, and mess facilities."
        ),
        (
            "Is there a library?",
            "Yes, the college has a well-equipped library."
        ),
        (
            "Are laboratories available?",
            "Yes, well-equipped laboratories are available for all departments."
        ),
        (
            "What sports facilities are available?",
            "Facilities for cricket, basketball, kabaddi, athletics, and indoor games are available."
        ),
        (
            "Are medical facilities available?",
            "Yes, medical facilities are available nearby for emergencies."
        ),

        # -------- PLACEMENTS & INTERNSHIPS --------
        (
            "What is the average placement package?",
            "The average placement package ranges from 3 LPA to 4.2 LPA."
        ),
        (
            "What is the highest placement package?",
            "The highest placement package offered is up to 8 LPA."
        ),
        (
            "Which companies visit for placements?",
            "TCS, Wipro, Infosys, Capgemini, Cognizant, Tech Mahindra, Oracle, Zomato, and other IT and core engineering companies visit for placements."
        ),
        (
            "Are internships provided?",
            "Yes, internships are provided through the Training and Placement Cell, including industry projects and research internships."
        ),

        # -------- STUDENT ACTIVITIES --------
        (
            "Does the college organize events?",
            "Yes, the college organizes technical fests, workshops, seminars, industrial visits, and cultural events such as Technospark and annual fests."
        ),
        (
            "Are there student clubs?",
            "Yes, student clubs include ACES (Computer), MESA (Mechanical), and EESA (E&TC)."
        ),
        (
            "Is NSS available?",
            "Yes, the college has an active NSS unit conducting social activities like tree plantation and voter awareness programs."
        ),

        # -------- CONTACT --------
        (
            "How can I contact the college?",
            "Address: Gat No. 441, A/P Kuran, Tal. Junnar, Dist. Pune – 410511. Phone: +91 9766463385. Email: jaihindprincipal7615@gmail.com. Website: https://jaihind.edu.in/jpk/"
        ),
        (
            "Can I take a campus tour?",
            "Yes, you can visit Jaihind College of Engineering for a campus tour during working hours. It is recommended to contact the admission office before visiting."
        ),
        (
            "I want a campus tour",
            "Yes, you can visit Jaihind College of Engineering for a campus tour during working hours. It is recommended to contact the admission office before visiting."
        ),
        (
            "Is campus tour available?",
            "Yes, campus tours are generally allowed during working hours. Please coordinate with the admission office before visiting."
        ),
        (
            "Can I visit campus before admission?",
            "Yes, prospective students can visit the campus before admission to understand the facilities and environment."
        ),

        # ---------- ACADEMIC ----------
        (
            "What is the medium of instruction?",
            "The medium of instruction at Jaihind College of Engineering is English."
        ),
        (
            "What is the duration of engineering course?",
            "The undergraduate engineering program has a duration of four years."
        ),
        (
            "Is attendance compulsory?",
            "Yes, students are required to maintain the minimum attendance as per university norms."
        ),
        (
            "How are exams conducted?",
            "Examinations are conducted as per the guidelines and schedule of Savitribai Phule Pune University."
        ),
        (
            "Are internal assessments conducted?",
            "Yes, internal assessments such as unit tests, assignments, and practical evaluations are conducted regularly."
        ),

        # ---------- FEES & SCHOLARSHIPS ----------
        (
            "What is the fee structure?",
            "The fee structure is decided by the Fee Regulating Authority and may change yearly. Please contact the college office for exact details."
        ),
        (
            "Are scholarships available?",
            "Yes, government and private scholarships are available for eligible students as per applicable rules."
        ),
        (
            "Can fees be paid in installments?",
            "Fee payment options and installment facilities can be confirmed with the college administration."
        ),

        # ---------- HOSTEL ----------
        (
            "Is hostel compulsory?",
            "No, hostel accommodation is optional and depends on student preference."
        ),
        (
            "Are hostel rooms shared?",
            "Hostel rooms are generally shared among students."
        ),
        (
            "Is food provided in the hostel?",
            "Yes, mess facilities are available for hostel students."
        ),
        (
            "Is there a warden in the hostel?",
            "Yes, hostels are supervised by wardens to ensure student safety and discipline."
        ),

        # ---------- TRANSPORT ----------
        (
            "Is there a bus facility?",
            "Yes, the college provides bus transportation from nearby locations based on student demand."
        ),
        (
            "Is the college easily reachable by public transport?",
            "Yes, the college is accessible by public transport and local travel options."
        ),

        # ---------- FACILITIES ----------
        (
            "Does the college have Wi-Fi?",
            "Yes, Wi-Fi and internet facilities are available on campus for academic use."
        ),
        (
            "Are computer labs available?",
            "Yes, well-equipped computer laboratories are available for students."
        ),
        (
            "Is there a canteen?",
            "Yes, the college has a canteen that provides food and refreshments to students."
        ),
        (
            "Is medical assistance available?",
            "Basic medical assistance is available, and nearby medical facilities can be accessed if required."
        ),
        (
            "Does Jaihind College have a library?",
            "Yes, the college has a well-equipped central library with academic books and digital resources."
        ),

        # ---------- PLACEMENT ----------
        (
            "Is placement compulsory for all students?",
            "Placement assistance is provided, but selection depends on student performance and company criteria."
        ),
        (
            "Does the college help with internships?",
            "Yes, students receive guidance and support for internships through departments and the placement cell."
        ),
        (
            "Are soft-skill or aptitude training sessions conducted?",
            "Yes, training sessions related to aptitude and communication skills are conducted for students."
        ),

        # ---------- CAMPUS LIFE ----------
        (
            "Does the college organize technical events?",
            "Yes, technical events, workshops, and seminars are organized regularly."
        ),
        (
            "Are cultural programs conducted?",
            "Yes, cultural programs and annual events are conducted for student engagement."
        ),
        (
            "Is NSS or social activity available?",
            "Yes, students can participate in social and community-oriented activities."
        ),

        # ---------- SAFETY ----------
        (
            "Is the campus ragging-free?",
            "Yes, the college follows strict anti-ragging rules as per government regulations."
        ),
        (
            "Is there security on campus?",
            "Yes, security staff are present on campus to ensure student safety."
        ),

        # ---------- CONTACT / VISIT ----------
        (
            "Whom should I contact for admission queries?",
            "You can contact the admission office or visit the college campus for detailed guidance."
        ),
        (
            "Can parents visit the college?",
            "Yes, parents are welcome to visit the campus during working hours."
        ),
# -------- STUDENT PERSPECTIVE & GENERAL QUESTIONS --------
(
    "Is the college good for computer engineering?",
    "Yes, Jai Hind College of Engineering offers Computer Engineering with experienced faculty, laboratories, and placement support."
),
(
    "Is this college good for placements?",
    "The college provides placement assistance through its Training and Placement Cell, and students are encouraged to improve skills for better opportunities."
),
(
    "Is Jai Hind College of Engineering a private or government college?",
    "Jai Hind College of Engineering is a private engineering college."
),
(
    "Is the college affiliated to SPPU?",
    "Yes, Jai Hind College of Engineering is affiliated with Savitribai Phule Pune University (SPPU)."
),
(
    "Is attendance strict in the college?",
    "Yes, students are expected to maintain attendance as per university and college rules."
),
(
    "Is there uniform in the college?",
    "Students are required to follow the dress code prescribed by the college."
),
(
    "How is college campus environment?",
    "The college provides a disciplined, academic-focused, and student-friendly campus environment."
),
(
    "Is the college safe for girls?",
    "Yes, the college campus follows safety guidelines, has security arrangements, and separate hostel facilities for girls."
),
(
    "Is ragging allowed in the college?",
    "No, the college follows strict anti-ragging rules as per government regulations."
),
(
    "Are first year students treated well?",
    "Yes, first-year students receive guidance from faculty and seniors in a supportive academic environment."
),
(
    "Does the college support extracurricular activities?",
    "Yes, students are encouraged to participate in technical, cultural, sports, and social activities."
),
(
    "Are industrial visits conducted?",
    "Yes, departments organize industrial visits to provide practical exposure to students."
),
(
    "Does the college provide project guidance?",
    "Yes, faculty members provide guidance for mini projects, final year projects, and research work."
),
(
    "Is WiFi free for students?",
    "WiFi and internet facilities are available on campus for academic purposes."
),
(
    "Is there a canteen on campus?",
    "Yes, the college has a canteen that provides food and refreshments."
),
(
    "Is there parking facility for students?",
    "Yes, parking facilities are available for students and staff within the campus."
),
(
    "Can students use laptops in college?",
    "Yes, students are allowed to use laptops for academic and project work."
),
(
    "Does the college conduct workshops and seminars?",
    "Yes, workshops, seminars, and guest lectures are conducted regularly."
),
(
    "Is the college suitable for rural students?",
    "Yes, the college focuses on technical education and development for students from rural backgrounds."
),
(
    "Does the college help students after graduation?",
    "Yes, the college provides career guidance, placement assistance, and alumni support."
),
(
    "Can students participate in competitions?",
    "Yes, students are encouraged to participate in technical competitions, hackathons, and cultural events."
),
(
    "Is there a friendly relationship between teachers and students?",
    "Yes, faculty members are approachable and supportive toward students."
),
(
    "Does the college focus on practical learning?",
    "Yes, the college emphasizes practical learning through labs, projects, and industrial exposure."
),
(
    "Is this college good for average students?",
    "Yes, the college supports students of all academic levels through mentoring and guidance."
),
(
    "Does the college provide career counseling?",
    "Yes, career counseling and guidance sessions are conducted for students."
)
    ]
)

cur.executemany(
    """
    INSERT INTO faq (question, answer)
    VALUES (?, ?)
    """,
    [
(
    "नमस्कार",
    "नमस्कार 😊 मी तुमची मदत करण्यासाठी इथे आहे."
),
(
    "तू कसा आहेस?",
    "मी छान आहे 😄 धन्यवाद! तुम्हाला कशाबद्दल माहिती हवी आहे?"
),
(
    "तू काय करत आहेस?",
    "मी विद्यार्थ्यांना कॉलेजविषयी माहिती देत आहे 😊"
),
(
    "धन्यवाद",
    "तुमचं स्वागत आहे 😊 अजून काही विचारायचं असेल तर सांगा."
),
(
    "बाय",
    "बाय 👋 शुभेच्छा!"
),
        # ---------------- MARATHI FAQ ----------------
        (
            "कॉलेज कुठे आहे?",
            "जय हिंद कॉलेज ऑफ इंजिनिअरिंग कुरण, तालुका जुन्नर, जिल्हा पुणे येथे स्थित आहे."
        ),
        (
            "प्रवेश प्रक्रिया काय आहे?",
            "प्रवेश MHT-CET/JEE गुणांवर आणि SPPU च्या नियमांनुसार केला जातो."
        ),
        (
            "वसतिगृह सुविधा आहे का?",
            "होय, विद्यार्थ्यांसाठी वसतिगृह सुविधा उपलब्ध आहे."
        ),
        (
            "कॉलेज बस सुविधा आहे का?",
            "होय, जवळच्या भागांमधून कॉलेज बस सेवा उपलब्ध आहे."
        ),
        (
            "कॅम्पस टूर मिळेल का?",
            "होय, तुम्ही कामकाजाच्या वेळेत कॅम्पस भेट देऊ शकता. प्रवेश कार्यालयाशी संपर्क साधा."
        ),
        (
            "शिष्यवृत्ती मिळते का?",
            "होय, पात्र विद्यार्थ्यांसाठी सरकारी शिष्यवृत्ती उपलब्ध आहे."
        ),
        (
            "कॉलेजमध्ये वाय-फाय आहे का?",
            "होय, कॅम्पसमध्ये शैक्षणिक वापरासाठी वाय-फाय उपलब्ध आहे."
        ),
        (
            "पालकांना भेट देता येते का?",
            "होय, पालक कामकाजाच्या वेळेत कॅम्पसला भेट देऊ शकतात."
        ),

        # ---------------- HINDI FAQ ----------------
(
    "नमस्ते",
    "नमस्ते 😊 मैं आपकी मदद के लिए यहाँ हूँ।"
),
(
    "आप कैसे हो?",
    "मैं बढ़िया हूँ 😄 पूछने के लिए धन्यवाद!"
),
(
    "आप क्या कर रहे हो?",
    "मैं छात्रों की कॉलेज से जुड़ी जानकारी में मदद कर रहा हूँ 😊"
),
(
    "धन्यवाद",
    "आपका स्वागत है 😊 अगर कुछ और पूछना हो तो बताइए।"
),
(
    "बाय",
    "अलविदा 👋 शुभकामनाएँ!"
),
        (
            "कॉलेज कहाँ है?",
            "जय हिंद कॉलेज ऑफ इंजीनियरिंग कुरण, तहसील जुन्नर, जिला पुणे में स्थित है।"
        ),
        (
            "एडमिशन प्रक्रिया क्या है?",
            "प्रवेश MHT-CET/JEE अंकों और SPPU के नियमों के अनुसार होता है।"
        ),
        (
            "क्या हॉस्टल सुविधा है?",
            "हाँ, छात्रों के लिए हॉस्टल सुविधा उपलब्ध है।"
        ),
        (
            "क्या कॉलेज बस सुविधा है?",
            "हाँ, आसपास के क्षेत्रों से कॉलेज बस सुविधा उपलब्ध है।"
        ),
        (
            "क्या मैं कैंपस टूर ले सकता हूँ?",
            "हाँ, आप कार्य समय में कैंपस विजिट कर सकते हैं। प्रवेश कार्यालय से संपर्क करें।"
        ),
        (
            "क्या स्कॉलरशिप मिलती है?",
            "हाँ, पात्र छात्रों के लिए सरकारी छात्रवृत्ति उपलब्ध है।"
        ),
        (
            "क्या कॉलेज में वाई-फाई है?",
            "हाँ, कैंपस में शैक्षणिक उपयोग के लिए वाई-फाई उपलब्ध है।"
        ),
        (
            "क्या माता-पिता कॉलेज आ सकते हैं?",
            "हाँ, माता-पिता कार्य समय में कैंपस विजिट कर सकते हैं।"
        )
    ]
)

conn.commit()
conn.close()

print("FAQ seed data inserted successfully")




