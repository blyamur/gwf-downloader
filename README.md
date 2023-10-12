## Script for downloading Google web fonts \ Скрипт для загрузки веб-шрифтов Google

A python script to download  `*.woff2` fonts from a source like:  `https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap` for further use on a web site from the local directory of the site.

The result of using the script, allows you to replace importing fonts from the view:  `@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;800;900&family=Roboto&display=swap');`

To the variant:

```
@font-face {.
  font-family: 'Nunito';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('../webfonts/XRXV3I6Li01BKofIOOaBXso.woff2') format('woff2');
  unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
}
```

This will store the required font locally and use it directly.

Скрипт на python для скачивания шрифтов формата  `*.woff2 ` с источника вида: `https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap` для дальнейшего использования на веб сайте из локальной директории сайта.

Результат использования скрипта, позволяет заменить импорт шрифтов с вида: `@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap');`

На вариант:

```
@font-face {
  font-family: 'Nunito';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('../webfonts/XRXV3I6Li01BKofIOOaBXso.woff2') format('woff2');
  unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
}
```

При этом необходимый шрифт будет храниться локально и использоваться напрямую.


## Usage | Использование 

Using the script is simple, just run the file `gwf-downloader.py`, and in the query field `Paste the link and press Enter / Вставьте ссылку и нажмите Enter:` insert a link like `https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap` and press enter. As a result, in the script directory, a folder `downloads` will be created where the fonts will be downloaded.

If at the very end of the script, the line `url = input("Paste the link and press Enter: ")` is replaced with `url = 'https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap'`, after running the script, the request to paste the link will not appear, the download will start automatically.

Использование скрипта простое, достаточно запустить файл  `gwf-downloader.py`, и в поле запроса  `Paste the link and press Enter / Вставьте ссылку и нажмите Enter:` вставить ссылку вида  `https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap`  и нажать enter. В результате выполнения, в директории скрипта, будет создана папка `downloads` куда и будут скачаны шрифты.

Если в самом конце скрипта, строку `url = input("Paste the link and press Enter: ")` заменить на `url = 'https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Roboto&display=swap'`, после запуска скрипта, запрос на вставку ссылки не появится, скачивание начнется автоматически.

- [x] Downloading in *.woff2 format \ Скачивание в формате *.woff2
- [x] You can set the link in the script itself \ Можно задать сссылку в самом скрипте
- [x] Task progress indication \ Индикация выполнения задачи

## License | Лицензия 

 It is important to always read the license for every font that you use. Each font family directory contains the appropriate license file for the fonts in that directory. The fonts files themselves also contain licensing and authorship metadata.

 Most of the fonts in the collection use the SIL Open Font License, v1.1. Some fonts use the Apache 2 license. The Ubuntu fonts use the Ubuntu Font License v1.0.
 
 The SIL Open Font License has an option for copyright holders to include a Reserved Font Name requirement, and this option is used with some of the fonts. If you modify those fonts, please take care of this important detail.

Важно всегда читать лицензию на каждый используемый шрифт. Каждый каталог семейства шрифтов содержит соответствующий файл лицензии для шрифтов в этом каталоге. Сами файлы шрифтов также содержат метаданные о лицензировании и авторстве.

Большинство шрифтов в коллекции используют лицензию SIL Open Font License, v1.1. Некоторые шрифты используют лицензию Apache 2. Шрифты Ubuntu используют лицензию Ubuntu Font License v1.0.

В лицензии SIL Open Font License предусмотрена возможность включения правообладателями требования о резервировании имени шрифта, и эта возможность используется в некоторых шрифтах. Если вы модифицируете эти шрифты, пожалуйста, обратите внимание на эту важную деталь.

## Links | Ссылки 

- [Google Fonts](https://fonts.google.com/)
- [Google for Developers](https://developers.google.com/fonts)
- [Google fonts on Github](https://github.com/google/fonts)
- [Python](https://www.python.org)

##  Terms and conditions | Условия
Not for commercial use. \ Не для коммерческого использования.

*Thanks for reading :heart_eyes_cat:* \  Спасибо за чтение!


### Did you find this useful?! | Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can buy me a cup of coffee :coffee: ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [ko-fi](https://ko-fi.com/W7W460SQ3) )*

Рад это слышать :) Если вы хотите мне помочь, вы можете угостить меня чашечкой кофе 
  
© 2023 From Russia with ❤ 
