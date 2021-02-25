import re
# Создаем список из обработанного словаря для дальнейшей записи в файл
def create_result_list(input_dict, dict_keys_list):
    reuslt_list = []
    for form in input_dict:
        reuslt = []
        for contacts in dict_keys_list:
            reuslt.append(input_dict[form][contacts])
        reuslt_list.append(reuslt)
    return reuslt_list




def result_sorting_the_file(pattern, input_file, pattern_to_sub):
    form_dict = {}
    pattern = re.compile(r"^([А-Я][а-я]+)?[\s\,]+([А-Я][а-я]+)?[\s\,]+([А-Я][а-я]+)?[\s\,]+([А-Я]+|[А-Я][а-я]+)?[\s\,]+([а-яёА-ЯЁa-zA-Z\s–]+)?[\s\,]+((\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s(-]*(\доб.)?[\s]?(\d+)?)?[\s\,]?(([a-zA-Z0-9.]+)?@?([a-zA-Z.]+)?)?")
    contacts_list_after_processing = []
    for contact in input_file:
        form = {}
        contacts_list_after_processing = pattern.sub(pattern_to_sub, ','.join(contact)).split(',')
        # Если ключ по фамилии уже есть в словаре, то работает с ним. Если нет - создаем
        if contacts_list_after_processing[0] not in form_dict:
            form_dict[contacts_list_after_processing[0]] = {
                                                            'email' : '',
                                                            'firstname' : '',
                                                            'lastname' : '',
                                                            'organization' : '',
                                                            'phone' : '',
                                                            'position' : '',
                                                            'surname' : ''
                                                            }
        # Записываем в словарь по ключу фамилии словарь со всеми даннымы пользователя
        for index, dict_key in enumerate(input_file[0]):
            if contacts_list_after_processing[index] != ' ':
                # Исключение с телефоном, так как у некоторых пользователей есть добавочный номер. Если он есть, то запись немного видоизменяем
                if dict_key == 'phone':
                    if len(contacts_list_after_processing[index]) == 18:
                        form_dict[contacts_list_after_processing[0]][dict_key] = contacts_list_after_processing[index]
                    elif len(contacts_list_after_processing[index]) == 22:
                        form_dict[contacts_list_after_processing[0]][dict_key] = contacts_list_after_processing[index][0:18] + 'доб.' + contacts_list_after_processing[index][-4:]
                else:
                    form_dict[contacts_list_after_processing[0]][dict_key] = contacts_list_after_processing[index]
    return form_dict
