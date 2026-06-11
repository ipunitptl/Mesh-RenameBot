
from dataclasses import dataclass

@dataclass
class HindiTranslations:
    LANGUAGE_NAME = "हिन्दी"
    LANGUAGE_CODE = "hi"

    WRONG_VALUE_ERROR = "❌ {{ variable_name }} वेरिएबल के लिए अमान्य मान दर्ज किया गया है।"

    START_MSG = (
        "👋 नमस्ते! मैं **Molly File Rename** हूँ।\n\n"
    )

    CANCEL_MESSAGE = "⚠️ नाम बदलना **रद्द** कर दिया गया है। जल्द ही अपडेट किया जाएगा।"

    RENAME_NO_FILTER_MATCH = (
        "🚫 **कोई फ़िल्टर मेल नहीं खाया - नाम बदलना रद्द किया जा रहा है**\n\n"
        "🔍 नाम निर्दिष्ट नहीं होने के कारण फ़िल्टर का उपयोग करके नाम बदला जा रहा है।\n"
        "📌 अपने फ़िल्टर को /filters का उपयोग करके प्रबंधित करें।"
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ नाम निर्दिष्ट नहीं होने के कारण फ़िल्टर का उपयोग करके नाम बदला जा रहा है।\n"
        "📌 अपने फ़िल्टर को /filters का उपयोग करके प्रबंधित करें।"
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ नया फ़ाइल नाम इस प्रारूप में दर्ज करें:\n"
        "```/rename my_new_filename.extension```\n"
        "या `/filters` का उपयोग करके नाम बदलने के फ़िल्टर सेट करें।"
    )

    RENAME_CANCEL = "❌ इस नाम बदलने को रद्द करें।"

    RENAMING_FILE = "🔄 फ़ाइल का नाम बदल रहा है... कृपया प्रतीक्षा करें।"

    DL_RENAMING_FILE = "📥 फ़ाइल डाउनलोड कर रहा है... कृपया प्रतीक्षा करें।"

    RENAME_ERRORED_REPORT = "❗ डाउनलोड में त्रुटि आई। इस समस्या की रिपोर्ट करें।"

    RENAME_CANCEL_BY_USER = "🚫 **उपयोगकर्ता द्वारा रद्द किया गया।**"

    FLTR_ADD_LEFT_STR = "➕ फ़िल्टर जोड़ा गया: `<code>{{ text_1 }}</code>` **बाएं तरफ**।"
    FLTR_ADD_RIGHT_STR = (
        "➕ फ़िल्टर जोड़ा गया: `<code>{{ text_1 }}</code>` **दाएं तरफ**।"
    )
    FLTR_RM_STR = "❌ फ़िल्टर हटाएं: `<code>{{ text_1 }}</code>`।"
    FLTR_REPLACE_STR = (
        "🔄 फ़िल्टर बदलें: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`।"
    )

    CURRENT_FLTRS = "⚙️ **आपके वर्तमान फ़िल्टर:**"
    ADD_FLTR = "➕ फ़िल्टर जोड़ें"
    RM_FLTR = "❌ फ़िल्टर हटाएं"

    FILTERS_INTRO = (
        "🛠 **फ़िल्टर गाइड:**\n"
        "फ़िल्टर के 3 प्रकार हैं:\n\n"
        "🔄 **बदलने वाला फ़िल्टर:** दिए गए शब्द को दूसरे शब्द से बदलें।\n"
        "➕ **जोड़ने वाला फ़िल्टर:** शुरुआत या अंत में एक शब्द जोड़ें।\n"
        "❌ **हटाने वाला फ़िल्टर:** फ़ाइलनाम से एक शब्द हटाएं।"
    )

    ADD_REPLACE_FLTR = "➕ बदलने वाला फ़िल्टर जोड़ें"
    ADD_ADDITION_FLTR = "➕ जोड़ने वाला फ़िल्टर जोड़ें"
    ADD_REMOVE_FLTR = "➕ हटाने वाला फ़िल्टर जोड़ें"
    BACK = "🔙 वापस"

    REPALCE_FILTER_INIT_MSG = "✍️ प्रारूप भेजें: `<code>बदलने_के_लिए_क्या | प्रतिस्थापन</code>` या वापस जाने के लिए `/ignore`।"

    NO_INPUT_FROM_USER = "⚠️ आपसे कोई इनपुट प्राप्त नहीं हुआ।"
    INPUT_IGNORE = "✅ **अवज्ञा की गई।**"
    WRONG_INPUT_FORMAT = "❌ अमान्य प्रारूप। कृपया दिए गए प्रारूप की जांच करें।"
    REPLACE_FILTER_SUCCESS = (
        "✅ **बदलने वाला फ़िल्टर जोड़ा गया:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ जोड़ने के लिए टेक्स्ट दर्ज करें `<code>|</code>` के साथ\n"
        "उदाहरण: `<code>| जोड़ने के लिए टेक्स्ट |</code>`\n"
        "या वापस जाने के लिए `/ignore`।"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ फ़िल्टर जोड़ा गया: `<code>{{ text_1 }}</code>` **बाएं तरफ**।"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ फ़िल्टर जोड़ा गया: `<code>{{ text_1 }}</code>` **दाएं तरफ**।"
    )

    ADDITION_LEFT = "🔄 बाएं तरफ जोड़ना"
    ADDITION_RIGHT = "🔄 दाएं तरफ जोड़ना"

    ADDITION_POSITION_PROMPT = "📍 **आप टेक्स्ट कहाँ जोड़ना चाहते हैं?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ वह टेक्स्ट दर्ज करें जिसे आप हटाना चाहते हैं या वापस जाने के लिए `/ignore`।"
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **हटाने वाला फ़िल्टर जोड़ा गया:** `<code>{{ text_1 }}</code>` हटाया जाएगा।"
    )

    REPLY_TO_MEDIA = "📂 एक मीडिया फ़ाइल को `/rename` के साथ जवाब दें।"

    RENAME_DOWNLOADING_DONE = "✅ डाउनलोड पूरा हुआ। अब फ़ाइल का नाम बदल रहा है..."
    RENAME_ERRORED = "❗ नाम बदलने की प्रक्रिया में त्रुटि आई।"
    RENAME_CANCEL_BY_USER = "🚫 **डाउनलोड रद्द कर दिया गया।**"

    UPLOADING_THE_FILE = "📤 फ़ाइल अपलोड कर रहा है: **{{ new_file_name }}**"

    RENAME_UPLOAD_CANCELLED_BY_USER = "🚫 **उपयोगकर्ता द्वारा अपलोड रद्द किया गया।**"
    RENAME_UPLOADING_DONE = "✅ **नाम बदलने की प्रक्रिया पूरी हो गई।**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **नाम बदलने के कार्य के लिए निष्पादन शुरू**\n"
        "🆔 कार्य आईडी: `{{ uid }}`\n\n"
        "👤 **उपयोगकर्ता नाम:** @{{ username }}\n"
        "📛 **नाम:** {{ name }}\n"
        "🆔 **उपयोगकर्ता आईडी:** `<code>{{ user_id }}</code>`\n"
        "📂 **फ़ाइल का नाम:** `<code>{{ file_name }}</code>`"
    )

    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **नाम बदलने का कार्य जोड़ा गया**\n\n"
        "👤 **उपयोगकर्ता नाम:** @{{ username }}\n"
        "📛 **नाम:** {{ name }}\n"
        "🆔 **उपयोगकर्ता आईडी:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "📌 **ध्यान दें:** आप `/setcaption` के साथ अपनी मनचाही टेक्स्ट का उपयोग करके कैप्शन सेट कर सकते हैं।\n"
        "📂 कैप्शन में नाम बदली गई फ़ाइल का नाम गतिशील रूप से डालने के लिए `<code>{file_name}</code>` का उपयोग करें।"
    )

    DELETE_CAPTION = "🗑 कैप्शन हटाएं"
    CLOSE = "❌ बंद करें"

    CAPTION_CURRENT = "📝 **आपका वर्तमान कैप्शन:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **कोई कैप्शन सेट नहीं है।**"
    CAPTION_SET = "✅ **कैप्शन अपडेट किया गया है:** {{ caption }}"
    CAPTION_DELETED = "🗑 **कैप्शन सफलतापूर्वक हटाया गया।**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **नाम बदलने का कार्य कतार में जोड़ा गया**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "📌 **मीडिया ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **नाम बदलने की कतार की स्थिति:**\n"
        "📌 **कतार में कुल कार्य:** {{ total_tasks }}\n"
        "📌 **कतार की क्षमता:** {{ queue_capacity }}\n"
        "⏳ **वर्तमान में प्रसंस्करण हो रहा है:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **आपका कार्य वर्तमान में निष्पादित हो रहा है**\n"
        "🆔 **कार्य आईडी:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **कतार में आपके कार्य की स्थिति:** {{ task_number }}\n"
        "🆔 **कार्य आईडी:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "🚷 **आपको चैट से हटा दिया गया है। आप इस बॉट का उपयोग नहीं कर सकते।**"
    USER_NOT_PARTICIPANT = "⚠️ **इस बॉट का उपयोग करने के लिए आवश्यक चैट में शामिल हों।**"
    JOIN_CHANNEL = "🔗 अपडेट चैनल में शामिल हों"

    MODE_INITIAL_MSG = (
        "📂 **फ़ाइल आउटपुट मोड:**\n\n"
        "1️⃣ **जैसा भेजा गया उसी प्रारूप में।**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **दस्तावेज़ पर मजबूरी।**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **सामान्य मीडिया के रूप में अपलोड करें।**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "📌 **नाम बदलने के मोड का चयन करें:**\n"
        "🅰️ **कमान्ड के साथ नाम बदलें।**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **कमान्ड के बिना नाम बदलें।**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 थंबनेल सेट करने के लिए एक छवि का उत्तर दें।"
    THUMB_SET_SUCCESS = "✅ **थंबनेल सफलतापूर्वक सेट किया गया।**"
    THUMB_NOT_FOUND = "⚠️ **कोई थंबनेल नहीं मिला।**"
    THUMB_CLEARED = "🗑 **थंबनेल सफलतापूर्वक साफ़ कर दिया गया।**"

    HELP_STR = (
        "📖 **बॉट कमांड्स:**\n"
        "`{{ startcmd }}` - ✅ जांचें कि बॉट चल रहा है या नहीं।\n"
        "`{{ renamecmd }}` - ✍️ एक मीडिया फ़ाइल का जवाब दें `/rename filename.extension` के साथ उसे नाम बदलने के लिए।\n"
        "`{{ filterscmd }}` - ⚙️ अपने नाम बदलने के फ़िल्टर प्रबंधित करें।\n"
        "`{{ setthumbcmd }}` - 📷 एक स्थायी थंबनेल सेट करें (एक छवि का उत्तर दें)।\n"
        "`{{ getthumbcmd }}` - 📸 वर्तमान में सेट किए गए थंबनेल प्राप्त करें।\n"
        "`{{ clrthumbcmd }}` - ❌ सेट किए गए थंबनेल को हटाएं।\n"
        "`{{ modecmd }}` - 🔄 3 आउटपुट मोड के बीच स्विच करें:\n"
        "    - 📝 जैसा भेजा गया उसी प्रारूप में।\n"
        "    - 📂 मजबूर दस्तावेज़।\n"
        "    - 🎥 सामान्य मीडिया (स्ट्रीम योग्य वीडियो/ऑडियो)।\n\n"
        "    🔄 नाम बदलने के मोड के बीच स्विच करें:\n"
        "    - 🏷 **कमान्ड** के साथ नाम बदलें।\n"
        "    - ✨ **कमान्ड** के बिना नाम बदलें।\n\n"
        "`{{ queuecmd }}` - 📊 बॉट की नाम बदलने की कतार की स्थिति देखें।\n"
        "`{{ setcaptioncmd }}` - 📝 नाम बदली गई फ़ाइलों के लिए कैप्शन सेट करें।\n"
        "`{{ helpcmd }}` - 📖 यह सहायता संदेश दिखाएं।\n"
        "`{{ setlaguagecmd }}` - 🌐 बॉट की भाषा सेट करें।\n"
    )

    CURRENT_LOCALE = "🌐 **आपकी वर्तमान भाषा:** {{ user_locale }}"
