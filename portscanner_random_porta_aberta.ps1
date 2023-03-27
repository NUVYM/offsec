# port scanner random porta aberta
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
$commonports = 21,22,80,443,3389
################################################################################################################## 
try {foreach ($porta in $commonports){
if (Test-NetConnection $endereco -Port $porta -WarningAction SilentlyContinue -InformationLevel Quiet){
	echo "Porta $porta aberta"
}} else {
	echo "Porta $porta fechada"
} 
} catch {}
}