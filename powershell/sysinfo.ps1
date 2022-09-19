function getIP{(get-netipaddress).ipv4address | Select-String "192*"}
function getUser { ($env:UserName.ToLower())}
function getHostName { ($env:USERDOMAIN.ToLower())}
function getPSV { ($Host.Version.Major)}
function getDate { (Get-Date -Format "dddd MM/dd/yyy")}


$IP = getIP
$User = getUser
$Hostname = getHostName
$PSV = getPSV
$Date = getDate
Write-Host("This machine's IP is $IP. User is $User. Hostname is $Hostname. Powershell Version $PSV. Today's date is $Date.")