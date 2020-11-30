Raccomandazioni tecniche per SOAP
=================================

In questo capitolo si raccolgono delle indicazioni per la tecnologia
SOAP, al fine di favorire l’interoperabilità.

[RAC_SOAP_001] Le API SOAP DEVONO rispettare il WS-I Basic Profile versione 2.0
-------------------------------------------------------------------------------

Questo profilo è definito dal WS-I (Web Services Interoperability
Organization), ora confluito in OASIS. Questa specifica è implementata
dai framework più diffusi.

[RAC_SOAP_002] Utilizzo di camelCase e PascalCase
-------------------------------------------------

Per i nomi dei servizi si DOVREBBE utilizzare PascalCase.

Per le operazioni implementate e gli argomenti si DOVREBBE utilizzare il
camelCase.

[RAC_SOAP_003] Unicità dei namespace e utilizzo di pattern fissi
----------------------------------------------------------------

All’interno del WSDL DOVREBBE essere presente un namespace unico.

[RAC_SOAP_004] Esporre lo stato del servizio
--------------------------------------------

L'API DEVE includere un metodo \`echo\` per restituire lo stato della
stessa.

ESEMPIO: Esposizione stato del servizio

+-----------------------------------------------------------------------+
| <?xml version="1.0" encoding="UTF-8"?>                                |
|                                                                       |
| <wsdl:definitions targetNamespace="http://www.example.com/webservice" |
|                                                                       |
| xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"                         |
|                                                                       |
| xmlns:xs="http://www.w3.org/2001/XMLSchema"                           |
|                                                                       |
| xmlns:ws="http://www.example.com/webservice">                         |
|                                                                       |
| <wsdl:types>                                                          |
|                                                                       |
| <xs:schema>                                                           |
|                                                                       |
| <xs:complexType name="userDefinedFault">                              |
|                                                                       |
| <xs:sequence>                                                         |
|                                                                       |
| <xs:element name="errorCode" type="xs:int"/>                          |
|                                                                       |
| <xs:element name="detail" type="xs:string"/>                          |
|                                                                       |
| <xs:element name="message" type="xs:string"/>                         |
|                                                                       |
| </xs:sequence>                                                        |
|                                                                       |
| </xs:complexType>                                                     |
|                                                                       |
| </xs:schema>                                                          |
|                                                                       |
| </wsdl:types>                                                         |
|                                                                       |
| <wsdl:message name="requestEcho">                                     |
|                                                                       |
| <wsdl:part name="msg" type="xs:string"/>                              |
|                                                                       |
| </wsdl:message>                                                       |
|                                                                       |
| <wsdl:message name="responseEcho">                                    |
|                                                                       |
| <wsdl:part name="msg" type="xs:string"/>                              |
|                                                                       |
| </wsdl:message>                                                       |
|                                                                       |
| <wsdl:message name="UserDefinedException">                            |
|                                                                       |
| <wsdl:part name="fault" type="userDefinedFault"/>                     |
|                                                                       |
| </wsdl:message>                                                       |
|                                                                       |
| <wsdl:portType name="portType">                                       |
|                                                                       |
| <wsdl:operation name="echo">                                          |
|                                                                       |
| <wsdl:input message="ws:requestEcho"/>                                |
|                                                                       |
| <wsdl:output message="ws:responseEcho"/>                              |
|                                                                       |
| <wsdl:fault name="fault" message="ws:UserDefinedException"/>          |
|                                                                       |
| </wsdl:operation>                                                     |
|                                                                       |
| </wsdl:portType>                                                      |
|                                                                       |
| </wsdl:definitions>                                                   |
+-----------------------------------------------------------------------+
