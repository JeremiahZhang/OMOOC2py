<!DOCTYPE >
<html>
    <body>
        <h1>Write new words into your diary.log:</h1>
        <form action="/write" method="get">
            <input type="text" size="100" maxlength="100" name="words" autofocus>
            <input type="submit" name="save" value="save">
        </form>
        <h1>  Darling!Here is your diary content!</h1>
        <textarea rows="30" cols="100">{{ content }}</textarea>
    </body>
</html>