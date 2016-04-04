# README #

### Зависимости ###

* Pillow
* selenium
* configparser
* pythonlangutil
* antigate

### Запуск ###

Для запуска необходимо в файле `/settings/base.py` в параметр `keywords` 
указать поисковое выражение. Далее в `state_value` указать страну. 
В файле `antigate.conf` заполнить соответствующие параметры.
Далее в `accounts.txt` нужно вписать данные от учетных записей, 
в формате `login:password`. Каждую учетную запись нужно вписывать с новой 
строки и без пробелов!
Для того чтобы указать тему и текст сообщения необходимо открыть файл
`message.txt`. В нем, первая строка это тема сообщения. Все что ниже само сообщение.

После этого необходимо выполнить следующие команды в консоле:
* `cd /`
* `source venv/bin/activate`
* `python3 run.py`

После этого начнется парсинг.

### Список стран и значений ###
* value="1" -> United States
* value="2" -> Canada
* value="3" -> United Kingdom
* value="4" -> Afghanistan
* value="5" -> Albania
* value="6" -> Algeria
* value="7" -> American Samoa
* value="8" -> Andorra
* value="9" -> Angola
* value="10" -> Anguilla
* value="11" -> Antigua and Barbuda
* value="12" -> Argentina
* value="13" -> Armenia
* value="14" -> Aruba
* value="15" -> Australia
* value="16" -> Austria
* value="17" -> Azerbaijan Republic
* value="18" -> Bahamas
* value="19" -> Bahrain
* value="20" -> Bangladesh
* value="21" -> Barbados
* value="22" -> Belarus
* value="23" -> Belgium
* value="24" -> Belize
* value="25" -> Benin
* value="26" -> Bermuda
* value="27" -> Bhutan
* value="28" -> Bolivia
* value="29" -> Bosnia and Herzegovina
* value="30" -> Botswana
* value="31" -> Brazil
* value="32" -> British Virgin Islands
* value="33" -> Brunei Darussalam
* value="34" -> Bulgaria
* value="35" -> Burkina Faso
* value="36" -> Burma
* value="37" -> Burundi
* value="38" -> Cambodia
* value="39" -> Cameroon
* value="40" -> Cape Verde Islands
* value="41" -> Cayman Islands
* value="42" -> Central African Republic
* value="43" -> Chad
* value="44" -> Chile
* value="45" -> China
* value="46" -> Colombia
* value="47" -> Comoros
* value="48" -> Congo, Democratic Republic of the
* value="49" -> Congo, Republic of the
* value="50" -> Cook Islands
* value="51" -> Costa Rica
* value="52" -> Cote d Ivoire (Ivory Coast)
* value="53" -> Croatia, Republic of
* value="55" -> Cyprus
* value="56" -> Czech Republic
* value="57" -> Denmark
* value="58" -> Djibouti
* value="59" -> Dominica
* value="60" -> Dominican Republic
* value="61" -> Ecuador
* value="62" -> Egypt
* value="63" -> El Salvador
* value="64" -> Equatorial Guinea
* value="65" -> Eritrea
* value="66" -> Estonia
* value="67" -> Ethiopia
* value="68" -> Falkland Islands (Islas Malvinas)
* value="69" -> Fiji
* value="70" -> Finland
* value="71" -> France
* value="72" -> French Guiana
* value="73" -> French Polynesia
* value="74" -> Gabon Republic
* value="75" -> Gambia
* value="76" -> Georgia
* value="77" -> Germany
* value="78" -> Ghana
* value="79" -> Gibraltar
* value="80" -> Greece
* value="81" -> Greenland
* value="82" -> Grenada
* value="83" -> Guadeloupe
* value="84" -> Guam
* value="85" -> Guatemala
* value="86" -> Guernsey
* value="87" -> Guinea
* value="88" -> Guinea-Bissau
* value="89" -> Guyana
* value="90" -> Haiti
* value="91" -> Honduras
* value="92" -> Hong Kong
* value="93" -> Hungary
* value="94" -> Iceland
* value="95" -> India
* value="96" -> Indonesia
* value="99" -> Ireland
* value="100" -> Israel
* value="101" -> Italy
* value="102" -> Jamaica
* value="104" -> Japan
* value="105" -> Jersey
* value="106" -> Jordan
* value="107" -> Kazakhstan
* value="108" -> Kenya
* value="109" -> Kiribati
* value="111" -> Korea, South
* value="112" -> Kuwait
* value="113" -> Kyrgyzstan
* value="114" -> Laos
* value="115" -> Latvia
* value="116" -> Lebanon
* value="120" -> Liechtenstein
* value="121" -> Lithuania
* value="122" -> Luxembourg
* value="123" -> Macau
* value="124" -> Macedonia
* value="125" -> Madagascar
* value="126" -> Malawi
* value="127" -> Malaysia
* value="128" -> Maldives
* value="129" -> Mali
* value="130" -> Malta
* value="131" -> Marshall Islands
* value="132" -> Martinique
* value="133" -> Mauritania
* value="134" -> Mauritius
* value="135" -> Mayotte
* value="136" -> Mexico
* value="226" -> Micronesia
* value="137" -> Moldova
* value="138" -> Monaco
* value="139" -> Mongolia
* value="228" -> Montenegro
* value="140" -> Montserrat
* value="141" -> Morocco
* value="142" -> Mozambique
* value="143" -> Namibia
* value="144" -> Nauru
* value="145" -> Nepal
* value="146" -> Netherlands
* value="147" -> Netherlands Antilles
* value="148" -> New Caledonia
* value="149" -> New Zealand
* value="150" -> Nicaragua
* value="151" -> Niger
* value="152" -> Nigeria
* value="153" -> Niue
* value="154" -> Norway
* value="155" -> Oman
* value="156" -> Pakistan
* value="157" -> Palau
* value="158" -> Panama
* value="159" -> Papua New Guinea
* value="160" -> Paraguay
* value="161" -> Peru
* value="162" -> Philippines
* value="163" -> Poland
* value="164" -> Portugal
* value="165" -> Puerto Rico
* value="166" -> Qatar
* value="227" -> Reunion
* value="167" -> Romania
* value="168" -> Russian Federation
* value="169" -> Rwanda
* value="170" -> Saint Helena
* value="171" -> Saint Kitts-Nevis
* value="172" -> Saint Lucia
* value="173" -> Saint Pierre and Miquelon
* value="174" -> Saint Vincent and the Grenadines
* value="175" -> San Marino
* value="176" -> Saudi Arabia
* value="177" -> Senegal
* value="229" -> Serbia
* value="178" -> Seychelles
* value="179" -> Sierra Leone
* value="180" -> Singapore
* value="181" -> Slovakia
* value="182" -> Slovenia
* value="183" -> Solomon Islands
* value="184" -> Somalia
* value="185" -> South Africa
* value="186" -> Spain
* value="187" -> Sri Lanka
* value="189" -> Suriname
* value="191" -> Swaziland
* value="192" -> Sweden
* value="193" -> Switzerland
* value="196" -> Taiwan
* value="197" -> Tajikistan
* value="198" -> Tanzania
* value="199" -> Thailand
* value="200" -> Togo
* value="201" -> Tonga
* value="202" -> Trinidad and Tobago
* value="203" -> Tunisia
* value="204" -> Turkey
* value="205" -> Turkmenistan
* value="206" -> Turks and Caicos Islands
* value="207" -> Tuvalu
* value="208" -> Uganda
* value="209" -> Ukraine
* value="210" -> United Arab Emirates
* value="211" -> Uruguay
* value="212" -> Uzbekistan
* value="213" -> Vanuatu
* value="214" -> Vatican City State
* value="215" -> Venezuela
* value="216" -> Vietnam
* value="217" -> Virgin Islands (U.S)
* value="218" -> Wallis and Futuna
* value="219" -> Western Sahara
* value="220" -> Western Samoa
* value="221" -> Yemen
* value="223" -> Zambia
* value="224" -> Zimbabwe