import streamlit as st
import time

st.set_page_config(page_title="RightBrothers", layout="wide")

# Sample translation dictionary
translations = {
    'Welcome to Lega Ease': {
        'hi': 'कानूनी अंतर्दृष्टि में आपका स्वागत है',
        'ta': 'சட்ட நுண்ணறிவுக்கு வரவேற்கிறோம்',
        'te': 'లీగల్ ఇన్సైట్స్‌కు స్వాగతం',
        'kn': 'ಕಾನೂನು ಒಳನೋಟಗಳಿಗೆ ಸುಸ್ವಾಗತ',
        'mr': 'कायदेशीर अंतर्दृष्टीस स्वागत आहे'
    },
    'Legal Dynamics': {
        'hi': 'कानूनी गतिशीलता',
        'ta': 'சட்ட இயக்கவியல்',
        'te': 'చట్ట డైనమిక్స్',
        'kn': 'ಕಾನೂನು ಡೈನಾಮಿಕ್ಸ್',
        'mr': 'कायदेशीर गतिशीलता'
    },
    'Legal Insights, Progress, and Advancements': {
        'hi': 'कानूनी अंतर्दृष्टि, प्रगति और उन्नति',
        'ta': 'சட்டத் தரவுகள், முன்னேற்றம் மற்றும் மேம்பாடுகள்',
        'te': 'చట్ట అంతర్దృష్టులు, పురోగతి మరియు అభివృద్ధులు',
        'kn': 'ಕಾನೂನು ಒಳನೋಟಗಳು, ಪ್ರಗತಿ ಮತ್ತು ಸುಧಾರಣೆಗಳು',
        'mr': 'कायदेशीर अंतर्दृष्टी, प्रगती आणि प्रगती'
    },
    'Stay informed with the latest legal insights, track progress, and witness industry advancements.': {
        'hi': 'नवीनतम कानूनी अंतर्दृष्टि के साथ सूचित रहें, प्रगति को ट्रैक करें, और उद्योग प्रगति का साक्षी बनें।',
        'ta': 'சமீபத்திய சட்டப் பார்வைகளுடன் புதுப்பிக்கவும், முன்னேற்றங்களைப் பின்தொடரவும் மற்றும் தொழில்துறை முன்னேற்றங்களைப் பாருங்கள்.',
        'te': 'తాజా చట్ట సమాచారంతో అప్డేట్ చేయబడండి, పురోగతిని ట్రాక్ చేయండి మరియు పరిశ్రమ పురోగతిని వీక్షించండి.',
        'kn': 'ತಾಜಾ ಕಾನೂನು ಮಾಹಿತಿ ಪಡೆಯಿರಿ, ಪ್ರಗತಿಯನ್ನು ಟ್ರಾಕ್ ಮಾಡಿ, ಮತ್ತು ಕೈಗಾರಿಕೆ ಪ್ರಗತಿಯನ್ನು ನೋಡಿರಿ.',
        'mr': 'नवीनतम कायदेशीर अंतर्दृष्टीसह अद्ययावत रहा, प्रगतीचे निरीक्षण करा, आणि उद्योगातील प्रगतीचा साक्षीदार बना.'
    },
    'Juridical Innovation': {
        'hi': 'न्यायिक नवाचार',
        'ta': 'நீதித்துறையின் புதுமை',
        'te': 'న్యాయ సాంకేతికత',
        'kn': 'ನ್ಯಾಯಿಕ ನಾವೀನ್ಯತೆ',
        'mr': 'न्यायालयीन नवोपक्रम'
    },
    'Legal Updates, Innovations, and Transformations': {
        'hi': 'कानूनी अपडेट्स, नवाचार और रूपांतरण',
        'ta': 'சட்ட புதுப்பிப்புகள், புதுமைகள் மற்றும் மாற்றங்கள்',
        'te': 'చట్ట అప్‌డేట్స్, నవీనతలు మరియు మార్పులు',
        'kn': 'ಕಾನೂನು ನವೀಕರಣಗಳು, ನಾವೀನ್ಯತೆಗಳು ಮತ್ತು ಪರಿವರ್ತನೆಗಳು',
        'mr': 'कायदेशीर अद्यतने, नवकल्पना आणि रूपांतरणे'
    },
    'Experience the legal landscape evolve through timely updates, innovative solutions, and transformative changes.': {
        'hi': 'समय पर अपडेट्स, नवाचारी समाधान और परिवर्तनकारी परिवर्तनों के माध्यम से कानूनी परिदृश्य का अनुभव करें।',
        'ta': 'சமயோசிதமான புதுப்பிப்புகள், புதுமையான தீர்வுகள் மற்றும் மாற்றத்திற்கான மாற்றங்களின் மூலம் சட்ட நிலப்பகுதியை அனுபவிக்கவும்.',
        'te': 'సమయానికి అనుగుణమైన అప్‌డేట్స్, సాంకేతిక పరిష్కారాలు మరియు పరివర్తనాత్మక మార్పుల ద్వారా చట్ట ప్రదేశాన్ని అనుభవించండి.',
        'kn': 'ಸಮಯೋಚಿತ ನವೀಕರಣಗಳು, ನಾವೀನ್ಯತೆ ಪರಿಹಾರಗಳು ಮತ್ತು ಪರಿವರ್ತನೆ ಬದಲಾವಣೆಗಳ ಮೂಲಕ ಕಾನೂನು ಲ್ಯಾಂಡ್‌ಸ್ಕೇಪ್ ಅನ್ನು ಅನುಭವಿಸಿ.',
        'mr': 'वेळेवर अद्यतने, नवकल्पक उपाय आणि परिवर्तनकारी बदलांद्वारे कायदेशीर क्षेत्राचा अनुभव घ्या.'
    },
    'Legislative Progression': {
        'hi': 'विधायी प्रगति',
        'ta': 'சட்ட மன்றத்தின் முன்னேற்றம்',
        'te': 'వ్యవస్థాపక పురోగతి',
        'kn': 'ಕಾನೂನು ಪ್ರಗತಿ',
        'mr': 'कायदे निर्मिती प्रगती'
    },
    'Legal Evolution, Progress, and Breakthroughs': {
        'hi': 'कानूनी विकास, प्रगति और सफलताएँ',
        'ta': 'சட்ட வளர்ச்சி, முன்னேற்றம் மற்றும் முக்கிய முறிவுகள்',
        'te': 'చట్ట అభివృద్ధి, పురోగతి మరియు బ్రేక్‌త్రూ',
        'kn': 'ಕಾನೂನು ಪ್ರಗತಿ, ಪ್ರಗತಿ ಮತ್ತು ಬ್ರೇಕ್‌ತ್ರೂ',
        'mr': 'कायदेशीर उत्क्रांती, प्रगती आणि यशस्वी'
    },
    'Witness the legal field\'s evolution, celebrate progress, and embrace groundbreaking breakthroughs.': {
        'hi': 'कानूनी क्षेत्र के विकास का गवाह बनें, प्रगति का जश्न मनाएं, और महत्वपूर्ण सफलताओं को अपनाएं।',
        'ta': 'சட்ட துறையின் முன்னேற்றத்தை காணுங்கள், முன்னேற்றத்தை கொண்டாடுங்கள் மற்றும் முக்கிய முறிவுகளை ஏற்றுக்கொள்ளுங்கள்.',
        'te': 'చట్ట రంగం యొక్క అభివృద్ధిని వీక్షించండి, పురోగతిని జరుపుకోండి మరియు బ్రేక్‌త్రూ ని ఆమోదించండి.',
        'kn': 'ಕಾನೂನು ಕ್ಷೇತ್ರದ ಪ್ರಗತಿಯನ್ನು ನೋಡಿರಿ, ಪ್ರಗತಿಯನ್ನು ಸಂಭ್ರಮಿಸಿ, ಮತ್ತು ಪ್ರಮುಖ ಯಶಸ್ಸನ್ನು ಅಳವಡಿಸಿಕೊಳ್ಳಿ.',
        'mr': 'कायदेशीर क्षेत्राच्या विकासाचा साक्षी बना, प्रगती साजरी करा आणि यशस्वीतेचा अंगीकार करा.'
    },
    'Judicial Advancement': {
        'hi': 'न्यायिक उन्नति',
        'ta': 'நீதித்துறையின் முன்னேற்றம்',
        'te': 'న్యాయ ప్రగతి',
        'kn': 'ನ್ಯಾಯ ಪ್ರಗತಿ',
        'mr': 'न्यायिक प्रगति'
    },
    'Legal Trends, Innovations, and Advancements': {
        'hi': 'कानूनी रुझान, नवाचार और उन्नति',
        'ta': 'சட்ட நவீனங்கள், புதுமைகள் மற்றும் முன்னேற்றங்கள்',
        'te': 'చట్ట పద్దతులు, సాంకేతికతలు మరియు అభివృద్ధులు',
        'kn': 'ಕಾನೂನು ಪ್ರವೃತ್ತಿಗಳು, ನಾವೀನ್ಯತೆಗಳು ಮತ್ತು ಪ್ರಗತಿಗಳು',
        'mr': 'कायदेशीर प्रवृत्त्या, नवकल्पना आणि प्रगती'
    },
    'Explore emerging legal trends, innovative solutions, and exciting advancements shaping the future.': {
        'hi': 'उभरते कानूनी रुझानों, नवाचारी समाधानों और रोमांचक उन्नति का अन्वेषण करें जो भविष्य को आकार दे रही हैं।',
        'ta': 'எதிர்காலத்தை வடிவமைக்கும் எழும் சட்ட நவீனங்கள், புதுமையான தீர்வுகள் மற்றும் சிறந்த முன்னேற்றங்களை ஆராயுங்கள்.',
        'te': 'భవిష్యత్తును ఆకారంలోకి తెస్తున్న ఉద్భవిస్తున్న చట్ట ధోరణులు, సాంకేతిక పరిష్కారాలు మరియు ఆసక్తికరమైన అభివృద్ధిని అన్వేషించండి.',
        'kn': 'ಭವಿಷ್ಯವನ್ನು ಆಕಾರಗೊಳಿಸುತ್ತಿರುವ ಉದಯಿಸುತ್ತಿರುವ ಕಾನೂನು ಪ್ರವೃತ್ತಿಗಳು, ನಾವೀನ್ಯತೆ ಪರಿಹಾರಗಳು ಮತ್ತು ರೋಮಾಂಚಕ ಪ್ರಗತಿಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.',
        'mr': 'भविष्यात आकार देणाऱ्या उदयोन्मुख कायदेशीर प्रवृत्त्या, नवकल्पक उपाय आणि रोमांचक प्रगतींचा शोध घ्या.'
    }
}

def translate_text(text, target_language):
    if text in translations and target_language in translations[text]:
        return translations[text][target_language]
    return text  # Return original text if no translation is available

def display_slideshow(images, delay=3):
    image_placeholder = st.empty()
    for i in range(len(images)):
        image_placeholder.image(images[i], use_column_width=True)
        time.sleep(delay)

def create_card(title, subtitle, date, description, image_url, color):
    st.markdown(
        f"""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <div style='display: flex;'>
                <div style='flex: 2;'>
                    <strong style='color: {color};'>{title}</strong>
                    <h3>{subtitle}</h3>
                    <div style='color: #6c757d;'>{date}</div>
                    <p>{description}</p>
                    <a href="#" style='color: #007bff;'>Continue reading</a>
                </div>
                <div style='flex: 1; margin-left: 20px;'>
                    <img src="{image_url}" width="200" height="250" style='border-radius: 10px;'>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    languages = {
        "English": "en",
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Kannada": "kn",
        "Marathi": "mr"
    }

    col1, col2 = st.columns([2, 1])
    with col2:
        selected_language = st.selectbox("Select Language", list(languages.keys()), key='language_selector')  # Add a key to prevent CSS conflicts

    target_language = languages[selected_language]

    if target_language != "en":
        st.title(translate_text('Welcome to LegaEase', target_language))
    else:
        st.title("Welcome to LegaEase")

    images = [
        'https://img.freepik.com/free-photo/still-life-with-scales-justice_23-2149776012.jpg?size=626&ext=jpg&ga=GA1.1.2008272138.1720569600&semt=sph',
        'https://images.moneycontrol.com/static-mcnews/2024/03/law-gender-rep.jpg?impolicy=website&width=770&height=431',
        'https://www.viveklawfirm.com/wp-content/uploads/2017/12/legal.jpg'
    ]

    # Display the slideshow
    display_slideshow(images)

    content = [
        {
            "title": "Legal Dynamics",
            "subtitle": "Legal Insights, Progress, and Advancements",
            "date": "Feb 12",
            "description": "Stay informed with the latest legal insights, track progress, and witness industry advancements.",
            "image_url": "https://i.pinimg.com/236x/e9/08/09/e90809ceb8b7b4c315464a6dbbf06b06.jpg",
            "color": "blue"
        },
        {
            "title": "Juridical Innovation",
            "subtitle": "Legal Updates, Innovations, and Transformations",
            "date": "Feb 11",
            "description": "Experience the legal landscape evolve through timely updates, innovative solutions, and transformative changes.",
            "image_url": "https://us.123rf.com/450wm/radiantskies/radiantskies1212/radiantskies121201290/16678674-abstract-word-cloud-for-judiciary-with-related-tags-and-terms.jpg",
            "color": "green"
        },
        {
            "title": "Legislative Progression",
            "subtitle": "Legal Evolution, Progress, and Breakthroughs",
            "date": "Feb 12",
            "description": "Witness the legal field's evolution, celebrate progress, and embrace groundbreaking breakthroughs.",
            "image_url": "https://dmgapc.com/attorney-torrance/images/dmgapc-stock1.jpg",
            "color": "red"
        },
        {
            "title": "Judicial Advancement",
            "subtitle": "Legal Trends, Innovations, and Advancements",
            "date": "Feb 11",
            "description": "Explore emerging legal trends, innovative solutions, and exciting advancements shaping the future.",
            "image_url": "https://thumbs.dreamstime.com/b/professional-female-lawyer-reviewing-legal-documents-modern-office-setting-lawsuit-preparation-examines-contract-related-323997651.jpg",
            "color": "orange"
        }
    ]

    if target_language != "en":
        for i in range(len(content)):
            content[i]['title'] = translate_text(content[i]['title'], target_language)
            content[i]['subtitle'] = translate_text(content[i]['subtitle'], target_language)
            content[i]['description'] = translate_text(content[i]['description'], target_language)

    for item in content:
        create_card(
            title=item['title'],
            subtitle=item['subtitle'],
            date=item['date'],
            description=item['description'],
            image_url=item['image_url'],
            color=item['color']
        )

if __name__ == "__main__":
    main()
