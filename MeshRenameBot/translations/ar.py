from dataclasses import dataclass

@dataclass
class ArabicTranslations:
    LANGUAGE_NAME = "العربية"
    LANGUAGE_CODE = "ar"

    WRONG_VALUE_ERROR = "❌ تم إدخال قيمة غير صالحة للمتغير {{ variable_name }}."

    START_MSG = (
        "👋 مرحبًا! أنا **Molly File Rename**.\n\n"
    )

    CANCEL_MESSAGE = "⚠️ تم **إلغاء** إعادة التسمية. سيتم التحديث قريبًا."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **لم يتطابق أي فلتر - إلغاء إعادة التسمية**\n\n"
        "🔍 يتم استخدام الفلاتر لإعادة التسمية لأنه لم يتم تحديد اسم.\n"
        "📌 قم بإدارة فلاترك باستخدام /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ يتم استخدام الفلاتر لإعادة التسمية لأنه لم يتم تحديد اسم.\n"
        "📌 قم بإدارة فلاترك باستخدام /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ أدخل اسم الملف الجديد بالتنسيق التالي:\n"
        "```/rename my_new_filename.extension```\n"
        "أو استخدم `/filters` لتعيين فلاتر إعادة التسمية."
    )

    RENAME_CANCEL = "❌ إلغاء إعادة التسمية هذه."

    RENAMING_FILE = "🔄 جاري إعادة تسمية الملف... يرجى الانتظار."

    DL_RENAMING_FILE = "📥 جاري تنزيل الملف... يرجى الانتظار."

    RENAME_ERRORED_REPORT = "❗ حدث خطأ أثناء التنزيل. يرجى الإبلاغ عن هذه المشكلة."

    RENAME_CANCEL_BY_USER = "🚫 **تم الإلغاء بواسطة المستخدم.**"

    FLTR_ADD_LEFT_STR = "➕ تمت إضافة فلتر: `<code>{{ text_1 }}</code>` **إلى اليسار**."
    FLTR_ADD_RIGHT_STR = (
        "➕ تمت إضافة فلتر: `<code>{{ text_1 }}</code>` **إلى اليمين**."
    )
    FLTR_RM_STR = "❌ إزالة فلتر: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 استبدال فلتر: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "⚙️ **فلاترك الحالية:**"
    ADD_FLTR = "➕ إضافة فلتر"
    RM_FLTR = "❌ إزالة فلتر"

    FILTERS_INTRO = (
        "🛠 **دليل الفلاتر:**\n"
        "هناك 3 أنواع من الفلاتر:\n\n"
        "🔄 **فلتر الاستبدال:** استبدل كلمة معينة بأخرى.\n"
        "➕ **فلتر الإضافة:** أضف كلمة في البداية أو النهاية.\n"
        "❌ **فلتر الإزالة:** أزل كلمة من اسم الملف."
    )

    ADD_REPLACE_FLTR = "➕ إضافة فلتر استبدال"
    ADD_ADDITION_FLTR = "➕ إضافة فلتر إضافة"
    ADD_REMOVE_FLTR = "➕ إضافة فلتر إزالة"
    BACK = "🔙 العودة"

    REPALCE_FILTER_INIT_MSG = "✍️ أرسل التنسيق: `<code>ما_يتم_استبداله | الاستبدال</code>` أو `/ignore` للرجوع."

    NO_INPUT_FROM_USER = "⚠️ لم يتم تلقي أي إدخال منك."
    INPUT_IGNORE = "✅ **تم التجاهل.**"
    WRONG_INPUT_FORMAT = "❌ تنسيق غير صالح. تحقق من التنسيق المقدم."
    REPLACE_FILTER_SUCCESS = (
        "✅ **تمت إضافة فلتر الاستبدال:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ أدخل النص الذي تريد إضافته باستخدام `<code>|</code>`\n"
        "مثال: `<code>| النص للإضافة |</code>`\n"
        "أو `/ignore` للرجوع."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ تمت إضافة فلتر: `<code>{{ text_1 }}</code>` **إلى اليسار**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ تمت إضافة فلتر: `<code>{{ text_1 }}</code>` **إلى اليمين**."
    )

    ADDITION_LEFT = "🔄 إضافة إلى اليسار"
    ADDITION_RIGHT = "🔄 إضافة إلى اليمين"

    ADDITION_POSITION_PROMPT = "📍 **أين تريد إضافة النص؟**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ أدخل النص الذي تريد إزالته أو `/ignore` للرجوع."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **تمت إضافة فلتر الإزالة:** سيتم إزالة `<code>{{ text_1 }}</code>`."
    )

    REPLY_TO_MEDIA = "📂 قم بالرد على ملف وسائط باستخدام `/rename`."

    RENAME_DOWNLOADING_DONE = "✅ اكتمال التنزيل. جارٍ الآن إعادة تسمية الملف..."
    RENAME_ERRORED = "❗ حدث خطأ أثناء عملية إعادة التسمية."
    RENAME_CANCEL_BY_USER = "🚫 **تم إلغاء التنزيل.**"

    UPLOADING_THE_FILE = "📤 جاري رفع الملف: **{{ new_file_name }}**"

    RENAME_UPLOAD_CANCELLED_BY_USER = "🚫 **تم إلغاء الرفع بواسطة المستخدم.**"
    RENAME_UPLOADING_DONE = "✅ **اكتملت عملية إعادة التسمية.**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **بدء التنفيذ لمهمة إعادة التسمية**\n"
        "🆔 معرف المهمة: `{{ uid }}`\n\n"
        "👤 **اسم المستخدم:** @{{ username }}\n"
        "📛 **الاسم:** {{ name }}\n"
        "🆔 **معرف المستخدم:** `<code>{{ user_id }}</code>`\n"
        "📂 **اسم الملف:** `<code>{{ file_name }}</code>`"
    )

    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **تمت إضافة مهمة إعادة التسمية**\n\n"
        "👤 **اسم المستخدم:** @{{ username }}\n"
        "📛 **الاسم:** {{ name }}\n"
        "🆔 **معرف المستخدم:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "📌 **ملاحظة:** يمكنك تعيين التسمية باستخدام `/setcaption` متبوعًا بالنص الذي تريده.\n"
        "📂 استخدم `<code>{file_name}</code>` لإدراج اسم الملف المعاد تسميته ديناميكيًا في التسمية."
    )

    DELETE_CAPTION = "🗑 حذف التسمية"
    CLOSE = "❌ إغلاق"

    CAPTION_CURRENT = "📝 **التسمية الحالية الخاصة بك:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **لم يتم تعيين تسمية.**"
    CAPTION_SET = "✅ **تم تحديث التسمية إلى:** {{ caption }}"
    CAPTION_DELETED = "🗑 **تم حذف التسمية بنجاح.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **تمت إضافة مهمة إعادة التسمية إلى الطابور**\n"
        "🆔 **معرف DC:** {{ dc_id }}\n"
        "📌 **معرف الوسائط:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **حالة طابور إعادة التسمية:**\n"
        "📌 **إجمالي المهام في الطابور:** {{ total_tasks }}\n"
        "📌 **سعة الطابور:** {{ queue_capacity }}\n"
        "⏳ **جارٍ المعالجة حاليًا:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **مهمتك قيد التنفيذ حاليًا**\n"
        "🆔 **معرف المهمة:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **موقع مهمتك في الطابور:** {{ task_number }}\n"
        "🆔 **معرف المهمة:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "🚷 **تمت إزالتك من الدردشة. لا يمكنك استخدام هذا البوت.**"
    USER_NOT_PARTICIPANT = "⚠️ **انضم إلى الدردشة المطلوبة لاستخدام هذا البوت.**"
    JOIN_CHANNEL = "🔗 انضم إلى قناة التحديثات"

    MODE_INITIAL_MSG = (
        "📂 **وضع إخراج الملف:**\n\n"
        "1️⃣ **نفس التنسيق كما تم الإرسال.**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **فرض كوثيقة.**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **رفع كوسائط عامة.**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "📌 **اختر وضع إعادة التسمية:**\n"
        "🅰️ **إعادة التسمية باستخدام الأمر.**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **إعادة التسمية بدون الأمر.**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 قم بالرد على صورة لتعيينها كصورة مصغرة."
    THUMB_SET_SUCCESS = "✅ **تم تعيين الصورة المصغرة بنجاح.**"
    THUMB_NOT_FOUND = "⚠️ **لم يتم العثور على صورة مصغرة.**"
    THUMB_CLEARED = "🗑 **تمت إزالة الصورة المصغرة بنجاح.**"

    HELP_STR = (
        "📖 **أوامر البوت:**\n"
        "`{{ startcmd }}` - ✅ تحقق مما إذا كان البوت يعمل.\n"
        "`{{ renamecmd }}` - ✍️ قم بالرد على ملف وسائط بـ `/rename filename.extension` لإعادة تسميته.\n"
        "`{{ filterscmd }}` - ⚙️ إدارة فلاتر إعادة التسمية الخاصة بك.\n"
        "`{{ setthumbcmd }}` - 📷 تعيين صورة مصغرة دائمة (قم بالرد على صورة).\n"
        "`{{ getthumbcmd }}` - 📸 الحصول على الصورة المصغرة الحالية.\n"
        "`{{ clrthumbcmd }}` - ❌ إزالة الصورة المصغرة المعينة.\n"
        "`{{ modecmd }}` - 🔄 التبديل بين 3 أوضاع إخراج:\n"
        "    - 📝 نفس التنسيق كما تم الإرسال.\n"
        "    - 📂 وثيقة مفروضة.\n"
        "    - 🎥 وسائط عامة (فيديو/صوت قابل للبث).\n\n"
        "    🔄 التبديل بين أوضاع إعادة التسمية:\n"
        "    - 🏷 إعادة التسمية **باستخدام الأمر**.\n"
        "    - ✨ إعادة التسمية **بدون استخدام الأمر**.\n\n"
        "`{{ queuecmd }}` - 📊 عرض حالة طابور إعادة التسمية للبوت.\n"
        "`{{ setcaptioncmd }}` - 📝 تعيين تسمية للملفات المعاد تسميتها.\n"
        "`{{ helpcmd }}` - 📖 عرض رسالة المساعدة هذه.\n"
        "`{{ setlanguagecmd }}` - 🌐 تغيير لغة البوت.\n"
    )

    CURRENT_LOCALE = "🌐 **لغتك الحالية:** {{ user_locale }}"
