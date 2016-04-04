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

* state_value="1" -> United States
* state_value="2" -> Canada
* state_value="3" -> United Kingdom
* state_value="4" -> Afghanistan
* state_value="5" -> Albania
* state_value="6" -> Algeria
* state_value="7" -> American Samoa
* state_value="8" -> Andorra
* state_value="9" -> Angola
* state_value="10" -> Anguilla
* state_value="11" -> Antigua and Barbuda
* state_value="12" -> Argentina
* state_value="13" -> Armenia
* state_value="14" -> Aruba
* state_value="15" -> Australia
* state_value="16" -> Austria
* state_value="17" -> Azerbaijan Republic
* state_value="18" -> Bahamas
* state_value="19" -> Bahrain
* state_value="20" -> Bangladesh
* state_value="21" -> Barbados
* state_value="22" -> Belarus
* state_value="23" -> Belgium
* state_value="24" -> Belize
* state_value="25" -> Benin
* state_value="26" -> Bermuda
* state_value="27" -> Bhutan
* state_value="28" -> Bolivia
* state_value="29" -> Bosnia and Herzegovina
* state_value="30" -> Botswana
* state_value="31" -> Brazil
* state_value="32" -> British Virgin Islands
* state_value="33" -> Brunei Darussalam
* state_value="34" -> Bulgaria
* state_value="35" -> Burkina Faso
* state_value="36" -> Burma
* state_value="37" -> Burundi
* state_value="38" -> Cambodia
* state_value="39" -> Cameroon
* state_value="40" -> Cape Verde Islands
* state_value="41" -> Cayman Islands
* state_value="42" -> Central African Republic
* state_value="43" -> Chad
* state_value="44" -> Chile
* state_value="45" -> China
* state_value="46" -> Colombia
* state_value="47" -> Comoros
* state_value="48" -> Congo, Democratic Republic of the
* state_value="49" -> Congo, Republic of the
* state_value="50" -> Cook Islands
* state_value="51" -> Costa Rica
* state_value="52" -> Cote d Ivoire (Ivory Coast)
* state_value="53" -> Croatia, Republic of
* state_value="55" -> Cyprus
* state_value="56" -> Czech Republic
* state_value="57" -> Denmark
* state_value="58" -> Djibouti
* state_value="59" -> Dominica
* state_value="60" -> Dominican Republic
* state_value="61" -> Ecuador
* state_value="62" -> Egypt
* state_value="63" -> El Salvador
* state_value="64" -> Equatorial Guinea
* state_value="65" -> Eritrea
* state_value="66" -> Estonia
* state_value="67" -> Ethiopia
* state_value="68" -> Falkland Islands (Islas Malvinas)
* state_value="69" -> Fiji
* state_value="70" -> Finland
* state_value="71" -> France
* state_value="72" -> French Guiana
* state_value="73" -> French Polynesia
* state_value="74" -> Gabon Republic
* state_value="75" -> Gambia
* state_value="76" -> Georgia
* state_value="77" -> Germany
* state_value="78" -> Ghana
* state_value="79" -> Gibraltar
* state_value="80" -> Greece
* state_value="81" -> Greenland
* state_value="82" -> Grenada
* state_value="83" -> Guadeloupe
* state_value="84" -> Guam
* state_value="85" -> Guatemala
* state_value="86" -> Guernsey
* state_value="87" -> Guinea
* state_value="88" -> Guinea-Bissau
* state_value="89" -> Guyana
* state_value="90" -> Haiti
* state_value="91" -> Honduras
* state_value="92" -> Hong Kong
* state_value="93" -> Hungary
* state_value="94" -> Iceland
* state_value="95" -> India
* state_value="96" -> Indonesia
* state_value="99" -> Ireland
* state_value="100" -> Israel
* state_value="101" -> Italy
* state_value="102" -> Jamaica
* state_value="104" -> Japan
* state_value="105" -> Jersey
* state_value="106" -> Jordan
* state_value="107" -> Kazakhstan
* state_value="108" -> Kenya
* state_value="109" -> Kiribati
* state_value="111" -> Korea, South
* state_value="112" -> Kuwait
* state_value="113" -> Kyrgyzstan
* state_value="114" -> Laos
* state_value="115" -> Latvia
* state_value="116" -> Lebanon
* state_value="120" -> Liechtenstein
* state_value="121" -> Lithuania
* state_value="122" -> Luxembourg
* state_value="123" -> Macau
* state_value="124" -> Macedonia
* state_value="125" -> Madagascar
* state_value="126" -> Malawi
* state_value="127" -> Malaysia
* state_value="128" -> Maldives
* state_value="129" -> Mali
* state_value="130" -> Malta
* state_value="131" -> Marshall Islands
* state_value="132" -> Martinique
* state_value="133" -> Mauritania
* state_value="134" -> Mauritius
* state_value="135" -> Mayotte
* state_value="136" -> Mexico
* state_value="226" -> Micronesia
* state_value="137" -> Moldova
* state_value="138" -> Monaco
* state_value="139" -> Mongolia
* state_value="228" -> Montenegro
* state_value="140" -> Montserrat
* state_value="141" -> Morocco
* state_value="142" -> Mozambique
* state_value="143" -> Namibia
* state_value="144" -> Nauru
* state_value="145" -> Nepal
* state_value="146" -> Netherlands
* state_value="147" -> Netherlands Antilles
* state_value="148" -> New Caledonia
* state_value="149" -> New Zealand
* state_value="150" -> Nicaragua
* state_value="151" -> Niger
* state_value="152" -> Nigeria
* state_value="153" -> Niue
* state_value="154" -> Norway
* state_value="155" -> Oman
* state_value="156" -> Pakistan
* state_value="157" -> Palau
* state_value="158" -> Panama
* state_value="159" -> Papua New Guinea
* state_value="160" -> Paraguay
* state_value="161" -> Peru
* state_value="162" -> Philippines
* state_value="163" -> Poland
* state_value="164" -> Portugal
* state_value="165" -> Puerto Rico
* state_value="166" -> Qatar
* state_value="227" -> Reunion
* state_value="167" -> Romania
* state_value="168" -> Russian Federation
* state_value="169" -> Rwanda
* state_value="170" -> Saint Helena
* state_value="171" -> Saint Kitts-Nevis
* state_value="172" -> Saint Lucia
* state_value="173" -> Saint Pierre and Miquelon
* state_value="174" -> Saint Vincent and the Grenadines
* state_value="175" -> San Marino
* state_value="176" -> Saudi Arabia
* state_value="177" -> Senegal
* state_value="229" -> Serbia
* state_value="178" -> Seychelles
* state_value="179" -> Sierra Leone
* state_value="180" -> Singapore
* state_value="181" -> Slovakia
* state_value="182" -> Slovenia
* state_value="183" -> Solomon Islands
* state_value="184" -> Somalia
* state_value="185" -> South Africa
* state_value="186" -> Spain
* state_value="187" -> Sri Lanka
* state_value="189" -> Suriname
* state_value="191" -> Swaziland
* state_value="192" -> Sweden
* state_value="193" -> Switzerland
* state_value="196" -> Taiwan
* state_value="197" -> Tajikistan
* state_value="198" -> Tanzania
* state_value="199" -> Thailand
* state_value="200" -> Togo
* state_value="201" -> Tonga
* state_value="202" -> Trinidad and Tobago
* state_value="203" -> Tunisia
* state_value="204" -> Turkey
* state_value="205" -> Turkmenistan
* state_value="206" -> Turks and Caicos Islands
* state_value="207" -> Tuvalu
* state_value="208" -> Uganda
* state_value="209" -> Ukraine
* state_value="210" -> United Arab Emirates
* state_value="211" -> Uruguay
* state_value="212" -> Uzbekistan
* state_value="213" -> Vanuatu
* state_value="214" -> Vatican City State
* state_value="215" -> Venezuela
* state_value="216" -> Vietnam
* state_value="217" -> Virgin Islands (U.S)
* state_value="218" -> Wallis and Futuna
* state_value="219" -> Western Sahara
* state_value="220" -> Western Samoa
* state_value="221" -> Yemen
* state_value="223" -> Zambia
* state_value="224" -> Zimbabwe