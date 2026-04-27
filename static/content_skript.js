let debounceTimer;

document.addEventListener('input', (event) => {
    // Очищаем таймер при каждом новом вводе
    clearTimeout(debounceTimer);

    // Устанавливаем новый таймер на 500 миллисекунд
    debounceTimer = setTimeout(() => {
        const activeElement = document.activeElement;
        
        // Проверяем, что это поле ввода, и оно не пустое
        if (activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA' || activeElement.isContentEditable) {
            const text = activeElement.value || activeElement.innerText;
            
            if (text.trim().length > 2) { // Не анализируем слишком короткие связки
                console.log("Юзер замолчал. Отправляем текст на проверку:", text);
                browser.runtime.sendMessage({ type: "CHECK_LAYOUT", text: text });
            }
        }
    }, 500); 
});