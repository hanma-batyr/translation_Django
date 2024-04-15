$(document).ready(function() {
    $('#translate-button').click(function(e) {
        e.preventDefault(); // Предотвращаем стандартное поведение формы
        translateText();
    });

    function translateText() {
        var sourceLang = $('#source-lang').val();
        var targetLang = $('#target-lang').val();
        var inputText = $('#input-text').val();

        var csrftoken = getCookie('csrftoken');

        var requestData = {
            'source_lang': sourceLang,
            'target_lang': targetLang,
            'input_text': inputText,
            'csrfmiddlewaretoken': csrftoken
        };

        $.ajax({
            type: 'POST',
            url: '{% url "index" %}', // Используем URL-шаблон для обработки POST-запроса
            data: requestData,
            success: function(response) {
                $('#output-text').val(response.result);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }


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
});


function swapLanguages() {
    var sourceLang = $('#source-lang').val();
    var targetLang = $('#target-lang').val();
    var inputText = $('#input-text').val();
    var outputText = $('#output-text').val();

    // Меняем местами исходный и целевой языки
    $('#source-lang').val(targetLang);
    $('#target-lang').val(sourceLang);

    // Меняем местами вводимый и выводимый тексты
    $('#input-text').val(outputText);
    $('#output-text').val(inputText);
}
