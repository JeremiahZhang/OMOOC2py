<p>Write new words into your diary.log:</p>
<form action="/write" method="GET">
<input type="text" size="100" maxlength="100" name="words" autofocus>
<input type="submit" name="save" value="save">
</form>

<p> Here is your diary content! Darling!</p>
<textarea rows="30" cols="100">{{ content }}</textarea>