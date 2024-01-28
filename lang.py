def change_lang(lang):

    Indonesia = {
        "title": "Pendeteksi Ujaran Kebencian",
        "desc": "Dalam Bahasa Indonesia",
        "text_input_placeholder": "Masukkan kalimat disini",
        "option": "Pilih bahasa antarmuka",
        "button": "Deteksi",
        "error": ":warning: Ujaran kebencian terdeteksi! harap lakukan hal berikut:",
        "write": "**1. Jangan Terlibat dalam Perdebatan atau Provokasi** <br> **2. Laporkan Ujaran Kebencian**",
        "success": ":heavy_check_mark: Tidak terdeteksi ujaran kebencian"
    }
    English = {
        "title": "Hate Speech Detector",
        "desc": "In Indonesia Language",
        "text_input_placeholder": "Enter a sentence here",
        "option": "Select language as interface",
        "button": "Detect",
        "error": ":warning: Hate speech detected! please do the following:",
        "write": "**1. Don't Engage in Arguments or Provocations** <br> **2. Report Hate Speech**",
        "success": ":heavy_check_mark: No hate speech detected"
    }
    korea = {
        "title": "증오심 표현 탐지기",
        "desc": "인도네시아 언어",
        "text_input_placeholder": "여기에 문장을 입력하세요",
        "option": "인터페이스로 언어 선택",
        "button": "감지",
        "error": ":warning: 증오심 표현이 감지되었습니다! 다음을 수행하세요:",
        "write": "**1. 논쟁이나 도발에 가담하지 마세요** <br> **2. 증오심 표현을 신고하세요**",
        "success": ":heavy_check_mark: 증오심 표현이 감지되지 않음"
    }

    if lang == "Indonesia":
        return Indonesia
    elif lang == "English":
        return English
    return korea
