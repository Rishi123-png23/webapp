import requests
import streamlit as st
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

#  find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "VJIT/RISHI_JRK" , page_icon ="https://vjit.ac.in/campus-life/clubs/#",layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.json()

hide_st_style = """
                <style>
                #MainMenu { visibility : hidden;}
                footer { visibility : hidden;}
                header { visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style , unsafe_allow_html = True)
                

# use local css
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
#animations

img_contact_form = Image.open("images/gdsc.png")
img_lottie_animation = Image.open("images/acm.jpeg")
img_dss_vjit = Image.open("images/dss.png")
img_code_vjit = Image.open("images/code.jpeg")
img_hita_vjit = Image.open("images/hita.jpg")
img_photo_vjit = Image.open("images/photo.jpg")
img_vjit = Image.open("images/vjit.png")
img_logo = Image.open("images/logo2.jpg")
img_bus = Image.open("images/vjitbus1.jpg")
img_study = Image.open("images/study.jpg")
img_dev = Image.open("images/dev1.jpg")
img_team = Image.open("images/team.jpeg")
img_place = Image.open("images/place.jpg")
img_street_vjit = Image.open("images/street.png")

st.image(img_logo,width = 220, use_column_width = 70 )
                                  

#horizontal menu
selected = option_menu(
        menu_title ="",
        options =["home","Activities","Academic","Links","Placement","Transport","Developer"],
        icons = ["house","globe","book","tv","book","pin-map","person-fill"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal")
        
if selected == "home":
              
              with st.container():
                    st.subheader("STUDENTS HELP DESK")
                    st.title(" VIDYA JYOTHI INSTITUTE OF TECHNOLOGY ")
                    st.image(img_vjit, caption = "VJIt")
              with st.container():
                    st.write("-----")
                    left_column,right_column = st.columns(2)
              with left_column:
                    st.header("VJIT,HYDERABAD,500065,TELANGANA")
                    st.write("##")
                    st.write(
            """
               - Accredited with A+ by the NAAC , and Ranked 200 in NIRF ranking 2022,
               - All B. Tech Programs have been accredited by NBA, Categorized as Band -Excellent (6-97 Ranking )
               - Institution in Atal Ranking of Institutions on Innovation Achievements (ARIIA-2021) by Ministry of Education, Government of India.
            """)
              with st.container():
                    st.write("-------")
                    st.header("QUERY BOX")
                    st.write("""
                                - This Query box is used to send your Query's to the Vjit official mail
                                - To know more about the College you can fill from and can submit
                                - If you have any problem with academics , Infrastructure , or any related problems with in the college you can fill the form and send the form
                                - Your  form will be seen by the Higher officails of our college, so their will sollution to Your problem. """)
                    st.subheader(" NOTE : YOUR FORM WILL BE SEND TO OUR OFFICIAL VJIT MAIL WITH YOUR DETAILS , SO ONLY IMPORTANT FORMS ARE ALLOWED TO BE SENT.")

                    contact_form = """
     <form action="https://formsubmit.co/bittuoggu1@gmail.com" method="POST">
     <input type = "hidden" name ="_captcha" value = "false">
     <input type="text" name="name" placeholder = "your name" required>
     <input type="email" name="email" placeholder = "your email" required>
     <textarea name = "message" placeholder = "Roll Number" required></textarea>
     <textarea name = "message" placeholder = "query" required></textarea>
     <button type= "submit">Send</button>
     </form>
     """
                    left_column,right_column = st.columns(2)
                    with left_column:
                        st.markdown(contact_form,unsafe_allow_html = True)
                    with right_column:
                        st.empty()

if selected == "Activities":
            with st.container():
                      st.write("-------")
                      st.header("VJIT ACTIVITIES")
                      st.write("##")
                      image_column,text_column = st.columns((1,2))
                      with image_column:
                           st.image(img_contact_form)
       

                      with text_column:
                           st.subheader("VJIT GDSC CLUB")
                           st.write(                                                                                                                                                                                                
                            """
                      Google Developer Student Clubs are university based community groups for students interested in Google developer technologies.
                      Students from all undergraduate or graduate programs with an interest in growing as a developer are welcome. By joining a GDSC,
                      students grow their knowledge in a peer-to-peer learning environment and build solutions for local businesses and their community.
   
                    - To conduct coding competitions.
                    - To establish a coding culture.
                    - Motivate students to learn programming with enthusiasm                                                                                                                                                                                   
                            """ 
                                )
                           st.markdown("[Instagram link..](https://www.instagram.com/gdscvjit)")
                           st.markdown("[registration link..](zCU8i4VCVhFLM8)")


            with st.container():
                    image_column,text_column = st.columns((1,2))
                    with image_column:
                         st.image(img_lottie_animation)

                    with text_column:
                        st.subheader("ACM VJIT")
                        st.write(
                   """
The Association for Computing Machinery (ACM) is an international learned society for computing.
It was founded in 1947, and is the world’s largest scientific and educational computing society.
ACM publishes over 50 journals including the prestigious Journal of the ACM, and two general magazines for computer professionals,
Communications of the ACM (also known as Communications or CACM) and Queue. 
As the world’s largest computing society, ACM strengthens the profession’s collective voice through strong leadership,
                   """                )
                        st.markdown("[contact info of VJITACM vice precident >](https://www.instagram.com/r_a_m_u_0_7/)")
 
             
            with st.container():
                 image_column,text_column = st.columns((1,2))
                 st.write("##")
                 with image_column:
                     st.image(img_dss_vjit)

                 with text_column:
                     st.subheader("DSS VJIT")
                     st.write(
                """
"Developer Student Society"  aims in providing an umbrella to the two existing clubs/groups at Department .
It also aims to provide infrastructure support i.e labs installed with Android Studio software to ease ,
existing Android and Web clubs to conduct workshops at Institution.
The student representatives/facilitators for the Developer Student Society from institution are mentored by Google trainers and are provided teaching materials to conduct development sessions at campus monthly.
Vidya Jyothi Institute of Technology, is the first in state of Telangana,
inaugurating the Developer Student Society comprising of both Applied CS with Android and Developer Student Club..
                   
         """ )
                     st.markdown("[dssvjit official page](https://vjit.ac.in/dss/)")
                     st.markdown("[dssvjit registration link >](https://developerssociety.typeform.com/to/gUmxYc?typeform-source=vjit.ac.in)")


        
 
            with st.container():
                  image_column,text_column = st.columns((1,2))
                  st.write("##")
                  with image_column:
                       st.image(img_code_vjit)

                  with text_column:
                       st.subheader("CODE CHEF VJIT")
                       st.write(
                """
The codechef club is related to programming club and Code-Chef is an online educational program and competitive programming community of global programmers. Code-Chef started as an educational initiative in 2009 by Directi, an Indian software company. In 2020, it became owned by Unacademy.

Along with monthly coding contests for the community, Code-Chef has initiatives for schools, colleges and women in competitive programming.
It hosted the India regionals of the ICPC for college students, as well as for the International Olympiad in Informatics (IOI), for school students in India.

Most parts of Code-Chef are available without charge.
                      """)
                       st.markdown("[codechef vjit official linkedin link >](https://www.linkedin.com/company/codechef-vjit/)")
            with st.container():
                  image_column,text_column = st.columns((1,2))
                  st.write("##")
                  with image_column:
                       st.image(img_hita_vjit)
                  with text_column:
                        st.subheader("HITA VJIT")
                        st.write("""
                                            
HITA is a student service club: where students are working with pleasure for the betterment and development of the society, helping and 
understanding the needs of the under privileged society.
HITIAN’s believes in the world of “Service to Mankind is Service to God” but this 
should be done with pleasure and hence it brought us the thought of forming a Club named – HITA

HITA
Institute encourages students to participate in extension activities and to help neighborhood community. Institute has different social activity 
clubs like HITA, Akrodh, AVASHAH-Hands that Help """)
                        st.markdown("[hita vjit official instagram link >](https://www.instagram.com/hita_vjit/)")
            with st.container():
                 image_column,text_column = st.columns((1,2))
                 st.write("##")
                 with image_column:
                     st.image(img_photo_vjit)

                 with text_column:
                     st.subheader("VJIT PHOTOGRAPHY CLUB")
                     st.write("""
                           Initialized by two students from First year B.Tech V Ranadheer, ECE and Subramanyam.
                           The VJIT-PHOTOGRAPHY CLUB joined the social networking site (Facebook) on 22 November 2013.
                           The students of VJIT showed a very keen interest and enthusiasm. Initially, the page received 200 plus likes.
                           All the nature-related photographs captured in VJIT and the events conducted in VJIT were posted on the page.
                           As the number of photographs increased the number of likes and comments reached peak levels.
                           The total number of likes in the VJIT- PHOTOGRAPHY CLUB is now 750 plus…..

The main intention behind this VJIT- PHOTOGRAPHY CLUB is to ignite interest among students in photography and aesthetic sense. """)
                     st.markdown("[VJIT PGC OFFICIAL FB LINK](https://www.facebook.com/VJITPGC/)")

            with st.container():
                 image_column,text_column = st.columns((1,2))
                 st.write("##")
                 with image_column:
                     st.image(img_street_vjit)

                 with text_column:
                     st.subheader("VJIT STREET CAUSE CLUB")
                     st.write("""Street Cause, a Hyderabad based student run NGO, which is spread across 30+ undergraduate institutions all over the twin cities. Street Cause is an 
NGO comprising of students who intend on doing their bit for the betterment of society with the objective of helping the underprivileged and 
destitute in every way possible. Every volunteer ensures utmost commitment and transparency throughout his/her term. The organization abides 
by its rules and keeps the incomes and expenses completely transparent.
Street Cause VJIT has won the “Best Youth Organization Award” in the year 2010. A few of the events have been conducted in collaboration with 
corporates such as Deloitte, Gold Drop Industries, Indian Red Cross Society and others. """)
                     st.markdown("[ VJIT STREET CAUSE OFFICIAL WEBSITE](http://streetcause.org/division_view/VJIT_eJRT)")
                
                             

if selected == "Academic":
             with st.container():
                  st.write("--------")
                  st.header(" Academic Resources of  Btech Four year's ")
                  st.image(img_study)
                  st.write( """
                          This sub website's basically consists of 1-4 years academic resourses of CSE,IT,AI,ECE and they are classified as 

                          - Text books.
                          - Lecturer's Notes.
                          - subject related pdf's.
                          - Previous year's Question papers.
                          - Question Banks.
                          - power point presentation of subjects.
                          - Hand written notes
                          - Question bank answers

                         """)
                                            
                  st.subheader("First year academic resourses")
                  st.write("This website consists of both academic semisters resoures of First year Btech")
                  st.markdown("[First year academic website>](https://itbnotes.netlify.app/)")
                  st.write("""
                                This website was created by our college student
                                - NAND KISHORE
                                - IT-B (First year) """)
                  st.markdown("[to know more about website developer>](https://www.linkedin.com/in/nand-kishore-809880172/)")
                                       
                  st.subheader("Second year academic resourses")
                  st.write("This website consists of both academic semisters resoures of Second year Btech")
                  st.write(" 1.Second year, First semister academic resourses")
                  st.markdown("[second year 1st sem academic resourses>](https://www.belvenkatesh.com/semester-1.html)")
                  st.write("  2.Second year , Second Semister academic resourses")
                  st.markdown("[second year 2nd sem academic resourses>](https://www.belvenkatesh.com/semester-2.html)")
                  st.subheader("Third year academic resourses")
                  st.write("This website consists of both academic semisters resourses of Third year Btech")
                  st.write(" 1.Third year , First semister academic resourses")
                  st.markdown("[Third year 1st sem academic semisters resourses>](https://www.belvenkatesh.com/semester-3-1.html)")
                  st.write("2.Third year, Second semister academic resourses")
                  st.markdown("[Third year 2nd sem academic resourses>](https://www.belvenkatesh.com/semester-3-2.html)")
                  st.write("NOTE : Second , Third,Fourth years academic resourses where gathered by = Mr.Belvenkatesh")
                  st.subheader("Fourth Year academic resourses")
                  st.markdown("[4th year academic resourses>](https://www.belvenkatesh.com/semester-4-1.html)")
                  st.header(" VJIT STUDENT HUB")
                  st.write("""
                             Vjit student hub was an platform in which you can improve you skills and this hub consists of :
                            - Mentors to guide us to improve our skills
                            - Resourses
                            - youtube Links
                            - Projects Ideas
                            - You can interact with other students and can form as a group to do a project
                            - Internships etc.. """)
                  st.markdown("[VJIT students Hub>](https://studentshubvjit.netlify.app/)")
                            
                              
                                 


if selected == "Transport":
          st.header(" VJIT TRANSPORT")
          st.write("""The college has its own fleet of buses operating from many points in the city of Hyderabad and the suburbs.
                      The starting points and routes of the College Buses: College Bus Timings & Route Details.
                       For more details contact Transport In-Charge Mr. D. Srinivas, 7396356323.""")
          st.image(img_bus)
          st.subheader("Route No.1 Bachupally :")
          st.write("""
                       - The college bus will be start at Nizampet at 7:35 and reaches to the college at 8:45 am
                       - The bus incharge is Mr.y praveen , contact (+91 9848622979) """)
          st.subheader("Route No.2 Pragathi Nagar :")
          st.write ("""
                       - The college bus will be start at pragathi nagar at 7:40 am and reaches to college at 8:45 am
                       - the bus incharge is Mr B.jagan , contact (+91 7416698273) """)
          st.subheader(" Route No.3 Nizampet X road :")
          st.write("""
                       - The college bus will be start at Nizampet X road at 7:40 am and reaches to college at 8:40 am
                       - The bus incharge is  Mr.A Sadanandam , contact (+91 9966146348) """)
          st.subheader("Route No.4 Bowenpally :")
          st.write ("""
                       - The college bus will be start at bowenpally at 7:20 am and reaches to college at 8:40 am
                       - The bus incharge is Mr M praveen , contact (+91 9676362613) """)
          st.subheader("Route NO.5 Ecil-Malkajgiri:")
          st.write("""
                       - The college bus will be start at Ecil at 7:05 am and reaches to college at 8:40 am
                       - The bus incharge is Mrs Sunitha rani , contact (+91 9885030764) """)
          st.subheader("Route No.6 Uppal :")
          st.write("""
                       - The college bus will start at boduppal at 7:15 am and reaches to college at 8:45 am
                       - the bus incharge is Mr. Nagaraju , contact (+91 8125899709)""")
          st.subheader("Route No.7 Ramanthapur :")
          st.write("""
                       - The college bus will be start at Nagole at 7:05 am and reaches to college at 8:45 am
                       - The bus incharge is Mr. Sridhar , contact (+91 9640802202)""")
          st.subheader("Route No.8 Lb Nagar :")
          st.write("""
                       - The bus will be start at Lb Nagar at 7:25 am and reaches to college at 8:50 am
                       - the bus incharge is Mrs. Bhavani , contact (+91 9963857515)""")
          st.subheader("Route No.9 Vansthalipuram:")
          st.write("""
                       - The bus will be start at Vansthalipuram ganesh temple at 7:40 am and reaches to college at 8:40 am
                       - The bus incharge is Mr. Govardhan , contact (+91 9395148232)""")
          st.subheader("Route No.10 Manikonda:")
          st.write("""
                       - The bus will be start at Manikonda (golden temple ) at 8:00 am and reaches to college at 8:40 am
                       """)
          st.subheader("Route No.11 Shaikpet :")
          st.write("""
                        - The bus will be start at Shaikpet(ioc pump) at 7:50 am and reaches to college at 8:40 am
                        - The bus incharge is Mrs A Swarna , contact (+91 9949922000) """)
          st.subheader("Route No.12 Attpur :")
          st.write("""
                       - The bus will be start at Gudimalkapur X road at 8:00 am and reaches to college at 8:40
                       - The bus incharge is Mr M Suresh , contact (+91 7658901000) """)
          st.subheader("Route No.13 Patancheru :")
          st.write("""
                      - The bus will be start at patancheru at 7:35 am and reaches to college at 8:45 am
                      - The bus incharge is Mrs.b shailaja , contact (+91 9963142619)""")
          st.subheader("Route No.14 Shankarpally:")
          st.write("""
                       - The bus will be start at Sangareddy at 7 :10 am and reaches to college at 8:40 am
                       - The bus incharge is Mr.Prakash , contact (+91 8143912645) """)
          st.subheader("Route No.15 Alwal:")
          st.write ("""
                       - The bus will be start at Alwal at 7:30 am and reaches to college at 8:35 am
                       """)
          st.subheader(" NOTE: The above information is taken from our offical college website, And to know more about the transportation click the bellow link")
          st.markdown("[VJIT transportation >](https://vjit.ac.in/about-us/infrastructure/)")

if selected == "Developer":
     
     with st.container():
          st.header("Further Development")
          st.subheader(" We are planning for further development , for any Information or development just fill the form and submit we contact you.")
          st.image(img_team)
          st.header("CONTACT US")
          contact_form = """
     <form action="https://formsubmit.co/rishikrishnajampala@gmail.com" method="POST">
     <input type = "hidden" name ="_captcha" value = "false">
     <input type="text" name="name" placeholder = "your name" required>
     <input type="email" name="email" placeholder = "your email" required>
     <textarea name = "Roll Number" placeholder = "your roll number" required></textarea>
     <textarea name = "Branch" placeholder = " your branch" required></textarea>
     <textarea name = "message" placeholder = "query" required></textarea>
     <button type= "submit">Send</button>
     </form>
     """
          left_column,right_column = st.columns(2)
          with left_column:
              st.markdown(contact_form,unsafe_allow_html = True)
          with right_column:
              st.empty()

     st.header("DEVELOPER INFO")
     with st.container():
          image_column,text_column = st.columns((1,2))
          with image_column:
              st.image(img_dev)

          with text_column:
              st.subheader("JAMPALA RISHI KRISHNA ")
              st.write("""
                              - (UI Designer,Software Architect, Product Owner for the project)
                              - 20911A6724
                              - COMPUTER SCIENCE AND ENGINEERING ( DATA SCIENCE), IIIrd year.
                       """)
              st.subheader("contact me")
              st.markdown("[contact me on Linkedin ](https://www.linkedin.com/in/jampala-rishi-krishna-215204201/)")
     st.write("------------")
     st.header(" They done a preponderance role in this prject")
     st.write(" - ROSHITH (20911A6720,CSE-DS)[ played major role in Code design , UI design]")
     st.write(" - Karthik (20911A6717,CSE-DS)[ Helped in code design ]")
     st.write(" - Rama Krishna(20911A6715, CSE-DS)[Helped in Code design]")
     st.subheader(" Major thanks for our team CONTROL FREAKS for being a major role in this project")
     st.write("-----------")
     st.subheader("Other than from our team")
     st.write(" - Jashvanth(20911A6740 , CSE-DS) [***  Information Gathering ,Idea's ***]")
     st.write(" - M.Nikhil(20911A6739, CSE-DS)[ Information Gathering ]")
     st.write(" - M.Alex(21915A6704),Daniel(20911A6713), CSE-DS)[ Editing ]")


if selected == "Links":
    st.header(" VJIT VARIOUS OFFICIAL WEBSITES")
    st.subheader("VJIT OFFICIAL WEBSITE ")
    st.write("""
                 For more information about the college you can visit the bellow link , The offical website mainly consist's of Info like :
                - Academic related information
                - Placement's related information
                - Courses
                - Sports
                - campus life
                - Infrastructure
                - Research.
            """)
    st.markdown("[VJIT OFFICIAL WEBSITE ](https://vjit.ac.in/)")
    st.write("-------")
    st.subheader(" VJIT STUDENT LOGIN")
    st.write("""
                 For more Information about the academics and student details you can visit the bellow link.
                 By login into the website with our login credentials we can visit the student login website and it mainly consists of Info like
                 - Student details
                 - Academic Information
                 - Exam fee payment
                 - course details
                 - NOTE:  WE CAN CHECK OUR SEMISTER RESULTS THROUGH THIS WEBSITE """)
    st.markdown("[VJIT STUDENT LOGIN](http://vjitautonomous.com/Login.aspx)")
    st.write("------")
    st.subheader("VJIT STUDENT FEE PAYMENT")
    st.write(" FOR PAYING ACADEMIC TUTION FEE OF THE COLLEGE YOU VISIT BELOW WEBSITE")
    st.markdown("[VJIT FEE PAYMENT](https://vjit.ac.in/online-fee-payment/)")



if selected == "Placement":
    st.header(" PLACEMENT'S PREPARATION")
    st.image(img_place)
    st.subheader("DOMAIN : ")
    st.header("NOTE : select your domain from bellow MENU BOX and start preparing")
    selected = option_menu(
        menu_title ="",
        options =["Aptitude","Logical Reasoning","programming"],
        icons = ["book","book","book"],
        menu_icon = "cast",
        orientation = "horizontal",
        default_index = 0)
    
    if selected == "Aptitude":
        st.header("QUANTITATIVE APTITUDE")
        st.write("Quantitative aptitude assesses a candiate analytical abilities.To succed in Quantitative of Algebra , Geometry,Trignometry,and Mensuration")
        st.subheader("How to Solve Quantitative Aptitude Questions Easily?")
        st.write("""
                   Follow the below steps 
                     - UNDERSTAND :
                     - Master the art of self-creating formulas by learning the concept from the brightest people and using the best shortcuts.
                     - PRACTICE :
                     - Practice all types of problems. Did you know that learning just a certain amount of problems in each subtopic is perfectly adequate.
                     - EVALUATE :
                     - Check your competency by writing some short, timed tests, and then enhance your ability by writing periodic tests.
                     - REPEAT :
                     - Redo the previous three steps for all the quantitative aptitude questions in order to get familiar with the topics. """)
        st.subheader("CONCEPTS")
        st.write("""
                     - AGES
                     - ARTHEMETIC PROGRESSION
                     - AVERAGE
                     - BOATS AND STREAMS
                     - CIRCLES
                     - COORDINATE GEOMETRY
                     - HCF and LCF
                     - LOGORITHM
                     - MENSURATION
                     - MIXTURES AND ALLIGATIONS
                     - PARTNERSHIP
                     - PERMUTATIONS AND COMBINATIONS
                     - PROBABILITY
                     - PROFIT AND LOSS
                     - RACES AND GAMES
                     - RATIO AND PROPORTION
                     - SIMPLE INTREST
                     - TIME AND WORK
                     - TIME,SPEED AND DISTANCE """)
        st.subheader("RESOURCES FOR PREPARATION ")
        st.subheader("complete aptitude playlist - RS AGGARWAL")
        st.write("click below link")
        st.markdown("[APTITUDE](https://www.youtube.com/watch?v=xeivfCIchmM&list=PLXjJ5c4vskp6yidDJs-NttEQwng8tu6Lo)")
    if selected == "Logical Reasoning":
        st.header("LOGICAL REASONING")
        st.write("""
                     - Logical reasoning refers to at least three different forms of reasoning.
                     - Deductive reasoning, inductive reasoning, and abductive reasoning are three types of reasoning that are based on deduction, induction, and abduction.
                     - The logical reasoning aptitude questions and answers assess a candidate's logical abilities.
                     """)
        st.subheader("CONCEPTS")
        st.write("""
                     - BLOOD RELATIONS
                     - CAUSE AND EFFECT
                     - CLOCK
                     - CODING AND DECODING
                     - DIRECTION AND CUBOIDS
                     - DIRECTION SENSE
                     - LETTER AND NUMBER SERIES
                     - OLD MAN OUT SERIES
                     - ODER AND RANKING
                     - SEATING AND ARRANGEMENT
                     - SYLLOGISM
                     - VENN DIAGRAMS
                     """)
        st.subheader("RESOURCES")
        st.subheader("complete logical reasoning playlist - CAREER RIDE ")
        st.write("click below link")
        st.markdown("[LOGICAL REASONING](https://www.youtube.com/watch?v=x0WkptLF6oE&list=PLpyc33gOcbVADMKqylI__O_O_RMeHTyNK)")

    if selected == "programming":
        st.header(" Compatitive Progamming Skills")
        st.subheader(" visit VJIT STUDENTS HUB website to improve your comptative programming skills")
        st.write("""
                        - STEP 1 : Go to home in website
                        - STEP 2 : Click on Academic
                        - STEP 3 : Scroll down , you will about VJIT STUDENTS HUB website and click on bellow link you will be redirected into the website
                        
                        """)
        
                    
               



st.write("---------------")

    






st.write("**********Copy Right @ 2022 |  Control Freaks | CSE-DS | created by RISHI|***********")
                         
                    
                                         
              

          
          
          


    
          

