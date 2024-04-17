$(document).ready(function() {
    // Ожидаем, пока весь HTML-документ загрузится
    $('#swap-languages').click(function() {
        // Обработчик клика на элементе с id "swap-languages"
        var sourceLang = $('#source_lang').val(); // Получаем значение исходного языка
        var targetLang = $('#target_lang').val(); // Получаем значение целевого языка
        
        // Меняем значения исходного и целевого языков местами
        $('#source_lang').val(targetLang);
        $('#target_lang').val(sourceLang);
    });
    
    $('#translation-form').submit(function(event) {
        // Обработчик отправки формы с id "translation-form"
        event.preventDefault(); // Предотвращаем стандартное поведение формы
        
        var form = $(this); // Получаем форму, отправленную пользователем
        var url = form.attr('action'); // Получаем URL для отправки AJAX-запроса
        
        // Отправляем асинхронный POST-запрос на сервер
        $.ajax({
            type: 'POST',
            url: url,
            data: form.serialize(), // Сериализуем данные формы
            success: function(data) {
                // Обработчик успешного выполнения запроса
                $('#translation-result').text(data.result); // Выводим результат перевода
            }
        });
    });
});
