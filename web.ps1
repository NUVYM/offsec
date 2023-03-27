# web
# Adiel Ribeiro
# 28set2022
# contato@nuvym.net
###############################################################################################################
## param ##
param($endereco)
###############################################################################################################
if(!$endereco){
	echo "Entre com o endereco"
} else {
###############################################################################################################
## var ## 
$web = Invoke-WebRequest -uri "$endereco" -Method Options
$web2 = Invoke-WebRequest -uri "$endereco"
###############################################################################################################
try {echo " "
echo "O servidor roda:" 
echo " "
$web.headers.server
echo " "
echo "O servidor aceita os metodos:"
echo " "
$web.headers.allow
echo " "
echo "Links encontrados:" 
echo " " 
$web2.links.href | Select-String "http://"
$web2.links.href | Select-String "https://"
} catch {}
}
