$(document).ready(function() {
    // Функция для получения CSRF-токена из куки
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    $('#translate-button').click(function() {
        var sourceLang = $('#source-lang').val();
        var targetLang = $('#target-lang').val();
        var inputText = $('#input-text').val();

        // Получаем CSRF-токен
        var csrftoken = getCookie('csrftoken');

        // Добавляем CSRF-токен к данным запроса
        var requestData = {
            'source_lang': sourceLang,
            'target_lang': targetLang,
            'input_text': inputText,
            'csrfmiddlewaretoken': csrftoken  // Добавляем CSRF-токен
        };

        $.ajax({
            type: 'POST',
            url: '/',
            data: requestData,
            success: function(response) {
                $('#output-text').val(response.result);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});