<!DOCTYPE html>
<html>
%from model.Thing import Thing
<head>
    <meta charset="UTF-8">
    <title>Test</title>
</head>

<body>
%thing = Thing('test description')
Content of the document......
<br />
{{thing.descr}}
</body>

</html>