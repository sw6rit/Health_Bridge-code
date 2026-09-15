import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageTk

# ==========================================
# 1. INTERNATIONALIZATION (i18n) DICTIONARY
# ==========================================
TRANSLATIONS = {
    "en": {
        "title": "🌸 HealthBridge - Kawaii Lifestyle Tracker 🌸",
        "user_profile": "🎀 User Profile",
        "name": "Name:",
        "age": "Age:",
        "language": "Language:",
        "tracking_inputs": "✨ Today's Wellness Inputs ✨",
        "sleep": "Sleep (Hours):",
        "hydration": "Water (Liters):",
        "steps": "Daily Step Count:",
        "exercise": "Exercise Duration (Mins):",
        "screen_time": "Screen Time (Hours):",
        "sports": "Sports / Active Play (Mins):",
        "aqi": "Current Local AQI:",
        "uv_index": "Current UV Index:",
        "select_exercise": "🏋️ Choose Exercise Pose:",
        "evaluate_btn": "💖 Calculate & Generate Report 💖",
        "report_title": "📊 Weekly Report & Gentle Insights 📊",
        "doctors_title": "🏥 Nearby Community Health Contacts",
        "aqi_good": "🌱 AQI is good! Great day for outdoor activities.",
        "aqi_bad": "😷 AQI is elevated. Prefer indoor workouts today!",
        "uv_high": "☀️ UV Index is high! Wear sunscreen and a hat outside.",
        "hydration_low": "💧 Water intake is low. Sip some fresh water!",
        "sleep_low": "😴 Sleep is below 7h. Try an early screen-free bedtime.",
        "screen_high": "📱 High screen time detected! Remember the 20-20-20 rule.",
    },
    "hi": {
        "title": "🌸 हेल्थब्रिज - जीवन शैली ट्रैकर 🌸",
        "user_profile": "🎀 उपयोगकर्ता प्रोफ़ाइल",
        "name": "नाम:",
        "age": "उम्र:",
        "language": "भाषा:",
        "tracking_inputs": "✨ आज के कल्याण इनपुट ✨",
        "sleep": "नींद (घंटे):",
        "hydration": "पानी (लीटर):",
        "steps": "दैनिक कदम:",
        "exercise": "व्यायाम (मिनट):",
        "screen_time": "स्क्रीन समय (घंटे):",
        "sports": "खेल / गतिविधियां (मिनट):",
        "aqi": "स्थानीय वायु गुणवत्ता (AQI):",
        "uv_index": "UV सूचकांक:",
        "select_exercise": "🏋️ व्यायाम मुद्रा चुनें:",
        "evaluate_btn": "💖 रिपोर्ट उत्पन्न करें 💖",
        "report_title": "📊 साप्ताहिक रिपोर्ट और सुझाव 📊",
        "doctors_title": "🏥 पास के सामुदायिक स्वास्थ्य संपर्क",
        "aqi_good": "🌱 वायु गुणवत्ता अच्छी है! बाहर टहलने जाएं।",
        "aqi_bad": "😷 हवा खराब है। आज घर के अंदर व्यायाम करें!",
        "uv_high": "☀️ UV अधिक है! बाहर निकलते समय सनस्क्रीन पहनें।",
        "hydration_low": "💧 पानी का सेवन कम है। पर्याप्त पानी पिएं!",
        "sleep_low": "😴 नींद कम है। रात को जल्दी सोने का प्रयास करें।",
        "screen_high": "📱 स्क्रीन समय अधिक है! आंखों को आराम दें।",
    },
    "kn": {
        "title": "🌸 ಹೆಲ್ತ್‌ಬ್ರಿಡ್ಜ್ - ಲೈಫ್‌ಸ್ಟೈಲ್ ಟ್ರ್ಯಾಕರ್ 🌸",
        "user_profile": "🎀 ಬಳಕೆದಾರರ ವಿವರ",
        "name": "ಹೆಸರು:",
        "age": "ವಯಸ್ಸು:",
        "language": "ಭಾಷೆ:",
        "tracking_inputs": "✨ ಇಂದಿನ ಆರೋಗ್ಯ ಮಾಹಿತಿ ✨",
        "sleep": "ನಿದ್ರೆ (ಗಂಟೆಗಳು):",
        "hydration": "ನೀರು (ಲೀಟರ್):",
        "steps": "ದೈನಂದಿನ ಹೆಜ್ಜೆಗಳು:",
        "exercise": "ವ್ಯಾಯಾಮ (ನಿಮಿಷಗಳು):",
        "screen_time": "ಸ್ಕ್ರೀನ್ ಸಮಯ (ಗಂಟೆಗಳು):",
        "sports": "ಕ್ರೀಡೆ / ಚಟುವಟಿಕೆ (ನಿಮಿಷಗಳು):",
        "aqi": "ಸ್ಥಳೀಯ ವಾಯು ಗುಣಮಟ್ಟ (AQI):",
        "uv_index": "UV ಸೂಚ್ಯಂಕ:",
        "select_exercise": "🏋️ ವ್ಯಾಯಾಮ ಭಂಗಿ ಆಯ್ಕೆಮಾಡಿ:",
        "evaluate_btn": "💖 ವರದಿ ಸಿದ್ಧಪಡಿಸಿ 💖",
        "report_title": "📊 ವಾರಾಂತ್ಯದ ವರದಿ ಮತ್ತು ಸಲಹೆಗಳು 📊",
        "doctors_title": "🏥 ಹತ್ತಿರದ ಸಮುದಾಯ ಆರೋಗ್ಯ ಸಂಪರ್ಕಗಳು",
        "aqi_good": "🌱 ಗಾಳಿಯ ಗುಣಮಟ್ಟ ಚೆನ್ನಾಗಿದೆ! ಹೊರಾಂಗಣ ಚಟುವಟಿಕೆಗೆ ಸೂಕ್ತ.",
        "aqi_bad": "😷 ಗಾಳಿಯ ಗುಣಮಟ್ಟ ಕಳಪೆಯಾಗಿದೆ. ಒಳಾಂಗಣ ವ್ಯಾಯಾಮ ಮಾಡಿ!",
        "uv_high": "☀️ UV ಸೂಚ್ಯಂಕ ಹೆಚ್ಚಾಗಿದೆ! ಸನ್‌ಸ್ಕ್ರೀನ್ ಬಳಸಿ.",
        "hydration_low": "💧 ನೀರಿನ ಸೇವನೆ ಕಡಿಮೆಯಾಗಿದೆ. ಹೆಚ್ಚು ನೀರು ಕುಡಿಯಿರಿ!",
        "sleep_low": "😴 ನಿದ್ರೆ ಕಡಿಮೆಯಾಗಿದೆ. ಬೇಗ ಮಲಗಲು ಪ್ರಯತ್ನಿಸಿ.",
        "screen_high": "📱 ಸ್ಕ್ರೀನ್ ಸಮಯ ಹೆಚ್ಚಾಗಿದೆ! ಕಣ್ಣುಗಳಿಗೆ ವಿಶ್ರಾಂತಿ ನೀಡಿ.",
    },
    "ta": {
        "title": "🌸 ஹெல்த்பிரிட்ஜ் - வாழ்க்கைமுறை ட்ராக்கர் 🌸",
        "user_profile": "🎀 பயனர் விவரம்",
        "name": "பெயர்:",
        "age": "வயது:",
        "language": "மொழி:",
        "tracking_inputs": "✨ இன்றைய ஆரோக்கிய தகவல்கள் ✨",
        "sleep": "தூக்கம் (மணிநேரம்):",
        "hydration": "நீர் (லிட்டர்):",
        "steps": "தினசரி அடிகள்:",
        "exercise": "உடற்பயிற்சி (நிமிடங்கள்):",
        "screen_time": "திரை நேரம் (மணிநேரம்):",
        "sports": "விளையாட்டு (நிமிடங்கள்):",
        "aqi": "காற்றின் தரம் (AQI):",
        "uv_index": "UV குறியீடு:",
        "select_exercise": "🏋️ உடற்பயிற்சி நிலையைத் தேர்ந்தெடுக்கவும்:",
        "evaluate_btn": "💖 அறிக்கையை உருவாக்கவும் 💖",
        "report_title": "📊 வாராந்திர அறிக்கை & ஆலோசனைகள் 📊",
        "doctors_title": "🏥 அருகில் உள்ள சுகாதார தொடர்புகள்",
        "aqi_good": "🌱 காற்றின் தரம் நன்று! வெளிப்புற பயிற்சிகளுக்கு ஏற்ற நாள்.",
        "aqi_bad": "😷 காற்று மாசு அதிகம். வீட்டிற்குள் உடற்பயிற்சி செய்யவும்!",
        "uv_high": "☀️ UV குடை குறியீடு அதிகம்! சன்ஸ்கிரீன் பயன்படுத்தவும்.",
        "hydration_low": "💧 குடிநீர் அளவு குறைவு. போதுமான அளவு நீர் அருந்தவும்!",
        "sleep_low": "😴 தூக்கம் போதாது. சீக்கிரம் தூங்க முயற்சிக்கவும்.",
        "screen_high": "📱 திரை நேரம் அதிகம்! கண்களுக்கு ஓய்வு கொடுங்கள்.",
    },
    "gu": {
        "title": "🌸 હેલ્થબ્રિજ - લાઈફસ્ટાઈલ ટ્રેકર 🌸",
        "user_profile": "🎀 વપરાશકર્તા પ્રોફાઇલ",
        "name": "નામ:",
        "age": "ઉંમર:",
        "language": "ભાષા:",
        "tracking_inputs": "✨ આજની વેલનેસ માહિતી ✨",
        "sleep": "ઊંઘ (કલાક):",
        "hydration": "પાણી (લીટર):",
        "steps": "દૈનિક પગલાં:",
        "exercise": "કસરત (મિનિટ):",
        "screen_time": "સ્ક્રીન સમય (કલાક):",
        "sports": "રમતગમત (મિનિટ):",
        "aqi": "હવાની ગુણવત્તા (AQI):",
        "uv_index": "UV ઇન્ડેક્સ:",
        "select_exercise": "🏋️ કસરતની સ્થિતિ પસંદ કરો:",
        "evaluate_btn": "💖 રિપોર્ટ બનાવો 💖",
        "report_title": "📊 સાપ્તાહિક રિપોર્ટ અને સલાહ 📊",
        "doctors_title": "🏥 નજીકના આરોગ્ય સંપર્કો",
        "aqi_good": "🌱 હવાની ગુણવત્તા સારી છે! બહાર જવા માટે ઉત્તમ દિવસ.",
        "aqi_bad": "😷 હવાનું પ્રદૂષણ વધુ છે. ઘરની અંદર કસરત કરો!",
        "uv_high": "☀️ UV ઇન્ડેક્સ વધુ છે! સનસ્ક્રીનનો ઉપયોગ કરો.",
        "hydration_low": "💧 પાણીનું પ્રમાણ ઓછું છે. વધુ પાણી પીઓ!",
        "sleep_low": "😴 ઊંઘ ઓછી છે. રાત્રે વહેલા સુવાનો પ્રયાસ કરો.",
        "screen_high": "📱 સ્ક્રીન સમય વધુ છે! આંખોને આરામ આપો.",
    },
    "mr": {
        "title": "🌸 हेल्थब्रिज - जीवनशैली ट्रॅकर 🌸",
        "user_profile": "🎀 वापरकर्ता प्रोफाइल",
        "name": "नाव:",
        "age": "वय:",
        "language": "भाषा:",
        "tracking_inputs": "✨ आजची आरोग्य माहिती ✨",
        "sleep": "झोप (तास):",
        "hydration": "पाणी (लीटर):",
        "steps": "दैनिक पावले:",
        "exercise": "व्यायाम (मिनिटे):",
        "screen_time": "स्क्रीन वेळ (तास):",
        "sports": "खेळ / खेळणे (मिनिटे):",
        "aqi": "हवेची गुणवत्ता (AQI):",
        "uv_index": "UV इंडेक्स:",
        "select_exercise": "🏋️ व्यायामाची पोझ निवडा:",
        "evaluate_btn": "💖 अहवाल तयार करा 💖",
        "report_title": "📊 साप्ताहिक अहवाल आणि सल्ला 📊",
        "doctors_title": "🏥 जवळील आरोग्य संपर्क",
        "aqi_good": "🌱 हवेची गुणवत्ता चांगली आहे! बाहेर फिरण्यास उत्तम दिवस.",
        "aqi_bad": "😷 हवेचे प्रदूषण जास्त आहे. घरातच व्यायाम करा!",
        "uv_high": "☀️ UV इंडेक्स जास्त आहे! सनस्क्रीन वापरा.",
        "hydration_low": "💧 पाणी कमी प्राशन केले आहे. भरपूर पाणी प्या!",
        "sleep_low": "😴 झोप अपुरी आहे. रात्री लवकर झोपण्याचा प्रयत्न करा.",
        "screen_high": "📱 स्क्रीन वेळ जास्त आहे! डोळ्यांना विश्रांती द्या.",
    },
    "bn": {
        "title": "🌸 হেলথব্রিজ - লাইফস্টাইল ট্র্যাকার 🌸",
        "user_profile": "🎀 ব্যবহারকারীর প্রোফাইল",
        "name": "নাম:",
        "age": "বয়স:",
        "language": "ভাষা:",
        "tracking_inputs": "✨ আজকের স্বাস্থ্য তথ্য ✨",
        "sleep": "ঘুম (ঘণ্টা):",
        "hydration": "জল (লিটার):",
        "steps": "দৈনিক পদক্ষেপ:",
        "exercise": "ব্যায়াম (মিনিট):",
        "screen_time": "স্ক্রিন টাইম (ঘণ্টা):",
        "sports": "খেলাধুলা (মিনিট):",
        "aqi": "বায়ুর মান (AQI):",
        "uv_index": "UV সূচক:",
        "select_exercise": "🏋️ ব্যায়ামের ভঙ্গি নির্বাচন করুন:",
        "evaluate_btn": "💖 রিপোর্ট তৈরি করুন 💖",
        "report_title": "📊 সাপ্তাহিক রিপোর্ট ও পরামর্শ 📊",
        "doctors_title": "🏥 নিকটস্থ স্বাস্থ্য কেন্দ্রসমূহ",
        "aqi_good": "🌱 বায়ুর মান ভালো! বাইরে ব্যায়াম করার উপযোগী দিন।",
        "aqi_bad": "😷 বায়ুদূষণ বেশি। ঘরের ভেতরে ব্যায়াম করুন!",
        "uv_high": "☀️ UV সূচক বেশি! বাইরে বের হলে সানস্ক্রিন ব্যবহার করুন।",
        "hydration_low": "💧 জল পানের পরিমাণ কম। পর্যাপ্ত জল পান করুন!",
        "sleep_low": "😴 ঘুম কম হয়েছে। রাতে তাড়াতাড়ি ঘুমানোর চেষ্টা করুন।",
        "screen_high": "📱 স্ক্রিন টাইম বেশি! চোখকে বিশ্রাম দিন।",
    },
    "ne": {
        "title": "🌸 हेल्थब्रिज - जीवनशैली ट्र्याकर 🌸",
        "user_profile": "🎀 प्रयोगकर्ता प्रोफाइल",
        "name": "नाम:",
        "age": "उमेर:",
        "language": "भाषा:",
        "tracking_inputs": "✨ आजको स्वास्थ्य विवरण ✨",
        "sleep": "निद्रा (घण्टा):",
        "hydration": "पानी (लिटर):",
        "steps": "दैनिक पाइला:",
        "exercise": "व्यायाम (मिनेट):",
        "screen_time": "स्क्रीन समय (घण्टा):",
        "sports": "खेलकुद (मिनेट):",
        "aqi": "हावाको गुणस्तर (AQI):",
        "uv_index": "UV सूचकांक:",
        "select_exercise": "🏋️ व्यायामको आसन रोज्नुहोस्:",
        "evaluate_btn": "💖 रिपोर्ट तयार गर्नुहोस् 💖",
        "report_title": "📊 साप्ताहिक रिपोर्ट र सुझावहरू 📊",
        "doctors_title": "🏥 नजिकैको स्वास्थ्य सम्पर्कहरू",
        "aqi_good": "🌱 हावाको गुणस्तर राम्रो छ! बाहिर घुम्न जानुहोस्।",
        "aqi_bad": "😷 हावा प्रदुषित छ। घरभित्रै व्यायाम गर्नुहोस्!",
        "uv_high": "☀️ UV सूचकांक उच्च छ! सनस्क्रीन प्रयोग गर्नुहोस्।",
        "hydration_low": "💧 पानीको मात्रा कम भयो। प्रशस्त पानी पिउनुहोस्!",
        "sleep_low": "😴 निद्रा अपुग छ। राति छिटो सुत्ने प्रयास गर्नुहोस्।",
        "screen_high": "📱 स्क्रीन समय धेरै भयो! आँखालाई आराम दिनुहोस्।",
    },
    "pa": {
        "title": "🌸 ਹੈਲਥਬ੍ਰਿਜ - ਲਾਈਫਸਟਾਈਲ ਟ੍ਰੈਕਰ 🌸",
        "user_profile": "🎀 ਉਪਭੋਗਤਾ ਪ੍ਰੋਫਾਈਲ",
        "name": "ਨਾਮ:",
        "age": "ਉਮਰ:",
        "language": "ਭਾਸ਼ਾ:",
        "tracking_inputs": "✨ ਅੱਜ ਦੇ ਸਿਹਤ ਅੰਕੜੇ ✨",
        "sleep": "ਨੀਂਦ (ਘੰਟੇ):",
        "hydration": "ਪਾਣੀ (ਲੀਟਰ):",
        "steps": "ਰੋਜ਼ਾਨਾ ਕਦਮ:",
        "exercise": "ਕਸਰਤ (ਮਿੰਟ):",
        "screen_time": "ਸਕ੍ਰੀਨ ਸਮਾਂ (ਘੰਟੇ):",
        "sports": "ਖੇਡਾਂ (ਮਿੰਟ):",
        "aqi": "ਹਵਾ ਦੀ ਗੁਣਵੱਤਾ (AQI):",
        "uv_index": "UV ਇੰਡੈਕਸ:",
        "select_exercise": "🏋️ ਕਸਰਤ ਦੀ ਪੋਜ਼ ਚੁਣੋ:",
        "evaluate_btn": "💖 ਰਿਪੋਰਟ ਤਿਆਰ ਕਰੋ 💖",
        "report_title": "📊 ਹਫ਼ਤਾਵਾਰੀ ਰਿਪੋਰਟ ਅਤੇ ਸੁਝਾਅ 📊",
        "doctors_title": "🏥 ਨੇੜਲੇ ਸਿਹਤ ਕੇਂਦਰਾਂ ਦੇ ਸੰਪਰਕ",
        "aqi_good": "🌱 ਹਵਾ ਦੀ ਗੁਣਵੱਤਾ ਵਧੀਆ ਹੈ! ਬਾਹਰ ਸੈਰ ਕਰਨ ਲਈ ਵਧੀਆ ਦਿਨ।",
        "aqi_bad": "😷 ਹਵਾ ਪ੍ਰਦੂਸ਼ਿਤ ਹੈ। ਘਰ ਦੇ ਅੰਦਰ ਹੀ ਕਸਰਤ ਕਰੋ!",
        "uv_high": "☀️ UV ਇੰਡੈਕਸ ਜ਼ਿਆਦਾ ਹੈ! ਸਨਸਕ੍ਰੀਨ ਦੀ ਵਰਤੋਂ ਕਰੋ।",
        "hydration_low": "💧 ਪਾਣੀ ਘੱਟ ਪੀਤਾ ਹੈ। ਹੋਰ ਪਾਣੀ ਪੀਓ!",
        "sleep_low": "😴 ਨੀਂਦ ਘੱਟ ਹੈ। ਰਾਤ ਨੂੰ ਜਲਦੀ ਸੌਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।",
        "screen_high": "📱 ਸਕ੍ਰੀਨ ਸਮਾਂ ਜ਼ਿਆਦਾ ਹੈ! ਅੱਖਾਂ ਨੂੰ ਆਰਾਮ ਦਿਓ।",
    },
    "ur": {
        "title": "🌸 ہیلتھ برج - لائف اسٹائل ٹریکر 🌸",
        "user_profile": "🎀 صارف کا پروفائل",
        "name": "نام:",
        "age": "عمر:",
        "language": "زبان:",
        "tracking_inputs": "✨ آج کی صحت کی تفصیلات ✨",
        "sleep": "نیند (گھنٹے):",
        "hydration": "پانی (لیٹر):",
        "steps": "روزانہ کے قدم:",
        "exercise": "ورزش (منٹ):",
        "screen_time": "اسکرین کا وقت (گھنٹے):",
        "sports": "کھیل (منٹ):",
        "aqi": "ہوا کی کوالٹی (AQI):",
        "uv_index": "یو وی انڈیکس:",
        "select_exercise": "🏋️ ورزش کی پوزیشن منتخب کریں:",
        "evaluate_btn": "💖 رپورٹ تیار کریں 💖",
        "report_title": "📊 ہفتہ وار رپورٹ اور تجاویز 📊",
        "doctors_title": "🏥 قریبی صحتی رابطے",
        "aqi_good": "🌱 ہوا کی کوالٹی اچھی ہے! باہر کی سرگرمیوں کے لیے بہترین دن۔",
        "aqi_bad": "😷 ہوا میں آلودگی زیادہ ہے۔ گھر کے اندر ورزش کریں!",
        "uv_high": "☀️ یو وی انڈیکس زیادہ ہے! سن اسکرین کا استعمال کریں۔",
        "hydration_low": "💧 پانی کا استعمال کم ہے۔ زیادہ پانی پیئیں!",
        "sleep_low": "😴 نیند پوری نہیں ہے۔ رات کو جلدی سونے کی کوشش کریں۔",
        "screen_high": "📱 اسکرین کا وقت زیادہ ہے! آنکھوں کو آرام دیں۔",
    }
}

# ==========================================
# 2. HELPER: DYNAMIC PASTEL POSE GENERATOR
# ==========================================
def create_pose_image(pose_name: str, color_hex: str) -> ImageTk.PhotoImage:
    """Generates a cute pastel illustrative placeholder image for exercise poses."""
    img = Image.new("RGB", (140, 140), color=color_hex)
    draw = ImageDraw.Draw(img)
    # Kawaii stick figure representations
    draw.ellipse((55, 20, 85, 50), fill="#FFF0F5", outline="#D8BFD8", width=3) # Head
    if pose_name == "Tree Pose (Balance)":
        draw.line((70, 50, 70, 100), fill="#D8BFD8", width=5) # Body
        draw.line((70, 60, 45, 35), fill="#D8BFD8", width=4) # Left Arm Up
        draw.line((70, 60, 95, 35), fill="#D8BFD8", width=4) # Right Arm Up
        draw.line((70, 100, 70, 130), fill="#D8BFD8", width=4) # Standing Leg
        draw.line((70, 80, 90, 95), fill="#D8BFD8", width=4) # Bent Leg
    elif pose_name == "Cobra Stretch (Back)":
        draw.line((40, 90, 70, 60), fill="#D8BFD8", width=5) # Torso up
        draw.line((70, 60, 120, 95), fill="#D8BFD8", width=5) # Legs down
        draw.line((55, 75, 55, 105), fill="#D8BFD8", width=4) # Arm support
    else: # Jumping Jacks / Active
        draw.line((70, 50, 70, 95), fill="#D8BFD8", width=5)
        draw.line((70, 60, 40, 30), fill="#D8BFD8", width=4)
        draw.line((70, 60, 100, 30), fill="#D8BFD8", width=4)
        draw.line((70, 95, 45, 125), fill="#D8BFD8", width=4)
        draw.line((70, 95, 95, 125), fill="#D8BFD8", width=4)
    
    return ImageTk.PhotoImage(img)

# ==========================================
# 3. BACKEND MODELS (OOP)
# ==========================================
class User:
    def __init__(self, name: str, age: int, lang: str = "en"):
        self.name = name
        self.age = age
        self.lang = lang

class WellnessRecord:
    def __init__(self, sleep: float, hydration: float, steps: int, exercise_mins: int, 
                 screen_hours: float, sports_mins: int, aqi: int, uv_index: int, pose: str):
        self.sleep = sleep
        self.hydration = hydration
        self.steps = steps
        self.exercise_mins = exercise_mins
        self.screen_hours = screen_hours
        self.sports_mins = sports_mins
        self.aqi = aqi
        self.uv_index = uv_index
        self.pose = pose

class WellnessReport:
    def __init__(self, user: User, record: WellnessRecord):
        self.user = user
        self.record = record

    def calculate_score(self) -> float:
        """Calculates a baseline wellness score out of 100."""
        score = 0.0
        # Sleep weight (20)
        score += min(20.0, (self.record.sleep / 8.0) * 20.0)
        # Hydration weight (20)
        score += min(20.0, (self.record.hydration / 2.5) * 20.0)
        # Movement weight (steps + exercise) (30)
        score += min(20.0, (self.record.steps / 8000.0) * 20.0)
        score += min(10.0, (self.record.exercise_mins / 30.0) * 10.0)
        # Screen time penalty (20 base)
        screen_pen = max(0.0, (self.record.screen_hours - 4.0) * 2.5)
        score += max(0.0, 20.0 - screen_pen)
        # AQI/UV modifier (10 base)
        score += 10.0 if self.record.aqi <= 100 else 5.0
        return round(min(100.0, score), 1)

    def generate_suggestions(self) -> list[str]:
        t = TRANSLATIONS.get(self.user.lang, TRANSLATIONS["en"])
        suggestions = []

        if self.record.sleep < 7.0:
            suggestions.append(t["sleep_low"])
        if self.record.hydration < 2.0:
            suggestions.append(t["hydration_low"])
        if self.record.screen_hours > 5.0:
            suggestions.append(t["screen_high"])
        
        # Environmental logic
        if self.record.aqi > 100:
            suggestions.append(t["aqi_bad"])
        else:
            suggestions.append(t["aqi_good"])
            
        if self.record.uv_index >= 6:
            suggestions.append(t["uv_high"])

        # Pose recommendation
        if self.record.pose == "Tree Pose (Balance)":
            suggestions.append("🧘 Tree Pose: Great choice! Focus on slow breathing and holding for 30s each leg.")
        elif self.record.pose == "Cobra Stretch (Back)":
            suggestions.append("🐍 Cobra Stretch: Excellent for countering long screen time and opening the chest.")
        else:
            suggestions.append("✨ Active Cardio: Keep your body warm and maintain a comfortable rhythm!")

        return suggestions

# ==========================================
# 4. FRONTEND / GUI LAYER (KAWAII PASTEL)
# ==========================================
class HealthBridgeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HealthBridge - Community Well-Being")
        self.geometry("820x900")
        self.configure(bg="#FFF0F5")  # Lavender Blush Pastel Background

        # Kawaii Theme Colors
        self.COLOR_BG = "#FFF0F5"
        self.COLOR_CARD = "#FFFFFF"
        self.COLOR_PINK = "#FFB6C1"
        self.COLOR_PASTEL_PURPLE = "#E6E6FA"
        self.COLOR_TEXT = "#4A4A4A"
        self.COLOR_BTN = "#FFC0CB"

        self.current_lang = "en"
        self.images_dict = {}
        
        # Supported languages mapping
        self.lang_options = {
            "English": "en",
            "Hindi": "hi",
            "Kannada": "kn",
            "Tamil": "ta",
            "Gujarati": "gu",
            "Marathi": "mr",
            "Bengali": "bn",
            "Nepali": "ne",
            "Punjabi": "pa",
            "Urdu": "ur"
        }

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=self.COLOR_BG)
        style.configure("Card.TFrame", background=self.COLOR_CARD, relief="flat")
        style.configure("Kawaii.TLabel", background=self.COLOR_CARD, foreground=self.COLOR_TEXT, font=("Comic Sans MS", 10, "bold"))
        style.configure("Title.TLabel", background=self.COLOR_BG, foreground="#FF69B4", font=("Comic Sans MS", 16, "bold"))
        style.configure("Kawaii.TButton", background=self.COLOR_BTN, foreground="#555555", font=("Comic Sans MS", 11, "bold"), borderwidth=0)
        style.map("Kawaii.TButton", background=[("active", "#FFB6C1")])

    def create_widgets(self):
        # Header
        self.header_label = ttk.Label(self, text=TRANSLATIONS["en"]["title"], style="Title.TLabel")
        self.header_label.pack(pady=10)

        # Main Container
        main_container = ttk.Frame(self)
        main_container.pack(fill="both", expand=True, padx=15, pady=5)

        # --- Top Bar: User & Language Profile ---
        profile_card = ttk.Frame(main_container, style="Card.TFrame")
        profile_card.pack(fill="x", pady=5, ipady=5, ipadx=10)

        ttk.Label(profile_card, text=TRANSLATIONS["en"]["user_profile"], style="Kawaii.TLabel").grid(row=0, column=0, columnspan=4, sticky="w", pady=2)
        
        ttk.Label(profile_card, text=TRANSLATIONS["en"]["name"], style="Kawaii.TLabel").grid(row=1, column=0, padx=5)
        self.ent_name = ttk.Entry(profile_card, width=12)
        self.ent_name.insert(0, "Aarya")
        self.ent_name.grid(row=1, column=1, padx=5)

        ttk.Label(profile_card, text=TRANSLATIONS["en"]["age"], style="Kawaii.TLabel").grid(row=1, column=2, padx=5)
        self.ent_age = ttk.Entry(profile_card, width=6)
        self.ent_age.insert(0, "20")
        self.ent_age.grid(row=1, column=3, padx=5)

        ttk.Label(profile_card, text="Lang:", style="Kawaii.TLabel").grid(row=1, column=4, padx=5)
        self.combo_lang = ttk.Combobox(profile_card, values=list(self.lang_options.keys()), state="readonly", width=10)
        self.combo_lang.current(0)
        self.combo_lang.grid(row=1, column=5, padx=5)
        self.combo_lang.bind("<<ComboboxSelected>>", self.on_language_change)

        # --- Form Grid Inputs ---
        input_card = ttk.Frame(main_container, style="Card.TFrame")
        input_card.pack(fill="x", pady=5, ipady=5, ipadx=10)

        ttk.Label(input_card, text=TRANSLATIONS["en"]["tracking_inputs"], style="Kawaii.TLabel").grid(row=0, column=0, columnspan=4, sticky="w", pady=5)

        # Input fields mapping
        self.inputs = {}
        fields = [
            ("sleep", "7.5", 1, 0), ("hydration", "2.1", 1, 2),
            ("steps", "6500", 2, 0), ("exercise", "25", 2, 2),
            ("screen_time", "4.0", 3, 0), ("sports", "20", 3, 2),
            ("aqi", "85", 4, 0), ("uv_index", "4", 4, 2)
        ]

        for key, default, r, c in fields:
            lbl = ttk.Label(input_card, text=TRANSLATIONS["en"][key], style="Kawaii.TLabel")
            lbl.grid(row=r, column=c, sticky="e", padx=5, pady=3)
            ent = ttk.Entry(input_card, width=10)
            ent.insert(0, default)
            ent.grid(row=r, column=c+1, sticky="w", padx=5, pady=3)
            self.inputs[key] = (lbl, ent)

        # --- Pose Selector with Visual Images ---
        pose_card = ttk.Frame(main_container, style="Card.TFrame")
        pose_card.pack(fill="x", pady=5, ipady=5, ipadx=10)

        self.lbl_select_pose = ttk.Label(pose_card, text=TRANSLATIONS["en"]["select_exercise"], style="Kawaii.TLabel")
        self.lbl_select_pose.pack(anchor="w")

        pose_frame = ttk.Frame(pose_card, style="Card.TFrame")
        pose_frame.pack(fill="x", pady=5)

        self.selected_pose = tk.StringVar(value="Tree Pose (Balance)")
        
        poses = [
            ("Tree Pose (Balance)", "#E6E6FA"),
            ("Cobra Stretch (Back)", "#FFE4E1"),
            ("Jumping Jacks (Cardio)", "#E0FFFF")
        ]

        for idx, (pose_name, color) in enumerate(poses):
            img_obj = create_pose_image(pose_name, color)
            self.images_dict[pose_name] = img_obj # Keep reference
            
            sub = ttk.Frame(pose_frame, style="Card.TFrame")
            sub.grid(row=0, column=idx, padx=20)

            lbl_img = tk.Label(sub, image=img_obj, bg=self.COLOR_CARD)
            lbl_img.pack()

            rb = tk.Radiobutton(sub, text=pose_name, value=pose_name, variable=self.selected_pose, 
                                bg=self.COLOR_CARD, font=("Comic Sans MS", 8, "bold"))
            rb.pack()

        # Submit Button
        self.btn_submit = ttk.Button(main_container, text=TRANSLATIONS["en"]["evaluate_btn"], style="Kawaii.TButton", command=self.evaluate)
        self.btn_submit.pack(pady=8)

        # --- Output & Suggestions Box ---
        out_card = ttk.Frame(main_container, style="Card.TFrame")
        out_card.pack(fill="both", expand=True, pady=5, ipadx=10, ipady=5)

        self.lbl_report = ttk.Label(out_card, text=TRANSLATIONS["en"]["report_title"], style="Kawaii.TLabel")
        self.lbl_report.pack(anchor="w")

        self.txt_output = tk.Text(out_card, height=7, bg="#FFF8DC", fg="#4A4A4A", font=("Comic Sans MS", 9), relief="flat")
        self.txt_output.pack(fill="both", expand=True, padx=5, pady=5)

        # --- Local Emergency Doctor Directory (SDG 10) ---
        doc_card = ttk.Frame(main_container, style="Card.TFrame")
        doc_card.pack(fill="x", pady=5, ipadx=10)

        self.lbl_docs = ttk.Label(doc_card, text=TRANSLATIONS["en"]["doctors_title"], style="Kawaii.TLabel")
        self.lbl_docs.pack(anchor="w")

        docs_text = "📞 Helpline: 104 (Health) | Community Care Center: +91 98765 43210 | Local Tele-Clinic: 1800-123-456"
        lbl_info = tk.Label(doc_card, text=docs_text, bg=self.COLOR_CARD, fg="#6A5ACD", font=("Comic Sans MS", 8, "bold"))
        lbl_info.pack(anchor="w", padx=5)

    def on_language_change(self, event):
        selected = self.combo_lang.get()
        self.current_lang = self.lang_options.get(selected, "en")
        t = TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"])

        # Update GUI texts dynamically
        self.header_label.config(text=t["title"])
        self.lbl_select_pose.config(text=t["select_exercise"])
        self.btn_submit.config(text=t["evaluate_btn"])
        self.lbl_report.config(text=t["report_title"])
        self.lbl_docs.config(text=t["doctors_title"])

        for key, (lbl, _) in self.inputs.items():
            lbl.config(text=t[key])

    def evaluate(self):
        try:
            # Type Conversion & Input Validation
            user = User(
                name=str(self.ent_name.get()),
                age=int(self.ent_age.get()),
                lang=self.current_lang
            )

            rec = WellnessRecord(
                sleep=float(self.inputs["sleep"][1].get()),
                hydration=float(self.inputs["hydration"][1].get()),
                steps=int(self.inputs["steps"][1].get()),
                exercise_mins=int(self.inputs["exercise"][1].get()),
                screen_hours=float(self.inputs["screen_time"][1].get()),
                sports_mins=int(self.inputs["sports"][1].get()),
                aqi=int(self.inputs["aqi"][1].get()),
                uv_index=int(self.inputs["uv_index"][1].get()),
                pose=self.selected_pose.get()
            )

            report = WellnessReport(user, rec)
            score = report.calculate_score()
            suggestions = report.generate_suggestions()

            # Render Results
            self.txt_output.delete("1.0", tk.END)
            self.txt_output.insert(tk.END, f"🌸 User: {user.name} | Overall Score: {score}/100 🌸\n")
            self.txt_output.insert(tk.END, "-" * 55 + "\n")
            for sug in suggestions:
                self.txt_output.insert(tk.END, f"• {sug}\n")

        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all entries contain valid numerical values!")

if __name__ == "__main__":
    app = HealthBridgeApp()
    app.mainloop()
