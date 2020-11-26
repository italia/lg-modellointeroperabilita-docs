[BLOCK_SOAP] Blocking SOAP
==========================

Se il pattern viene implementato con tecnologia SOAP, a differenza del
caso REST, il metodo invocato non è specificato nell’endpoint chiamato,
poiché viene identificato all’interno del body. Inoltre tutti gli ID
coinvolti DEVONO essere riportati all’interno del body. DEVE essere
rispettata le seguente regola:

-  la specifica dell’interfaccia dell’erogatore DEVE dichiarare tutti i
   metodi esposti con relativi schemi dei messaggi di richiesta e di
   ritorno. Inoltre le interfacce devono specificare eventuali header
   SOAP richiesti.

   3. .. rubric:: Regole di processamento
         :name: regole-di-processamento-1

Nel caso di errore il WS-I Basic Profile Version 2.0 richiede l’utilizzo
del meccanismo della SOAP fault per descrivere i dettagli dell’errore.
Al ricevimento della richiesta da parte del fruitore, l’erogatore:

-  DEVE verificare la validità sintattica dei dati in ingresso. In caso
   di dati errati DEVE restituire HTTP status 500 Internal Server Error
   fornendo dettagli circa l’errore utilizzando il meccanismo della SOAP
   fault;

-  Se l’erogatore ipotizza che la richiesta sia malevola PUÒ ritornare
   HTTP status 400 Bad Request o HTTP status 404 Not Found

-  In caso di errori non dipendenti dal fruitore, DEVE restituire i
   codici HTTP 5XX rispettando la semantica degli stessi o restituire il
   codice HTTP status 500 Internal Server Error indicando il motivo
   dell’errore nella SOAP fault;

-  In caso di successo restituire HTTP status 200 OK, riempiendo il body
   di risposta con il risultato dell’operazione.

   4. .. rubric:: Esempio
         :name: esempio-1

Specifica Servizio

https://api.ente.example/soap/nome-api/v1?wsdl

+-----------------------------------------------------------------------+
| <?xml version='1.0' encoding='UTF-8'?>                                |
|                                                                       |
| **<wsdl:definitions**                                                 |
|                                                                       |
| xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"                         |
|                                                                       |
| xmlns:tns="http://ente.example/nome-api"                              |
|                                                                       |
| xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap12/"                  |
|                                                                       |
| name="SOAPBlockingImplService"                                        |
|                                                                       |
| targetNamespace="http://ente.example/nome-api"\ **>**                 |
|                                                                       |
| **<wsdl:types>**                                                      |
|                                                                       |
| **<xs:schema**                                                        |
|                                                                       |
| xmlns:xs="http://www.w3.org/2001/XMLSchema"                           |
|                                                                       |
| xmlns:tns="http://ente.example/nome-api"                              |
|                                                                       |
| attributeFormDefault="unqualified" elementFormDefault="unqualified"   |
|                                                                       |
| targetNamespace="http://ente.example/nome-api"\ **>**                 |
|                                                                       |
| **<xs:element** name="MRequest" type="tns:MRequest"\ **/>**           |
|                                                                       |
| **<xs:element** name="MRequestResponse"                               |
| type="tns:MRequestResponse"\ **/>**                                   |
|                                                                       |
| **<xs:complexType** name="MRequest"\ **>**                            |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="M" type="tns:mType"\ **/>**       |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="mType"\ **>**                               |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="oId" type="xs:int"\ **/>**        |
|                                                                       |
| **<xs:element** minOccurs="0" name="a"                                |
| type="tns:aComplexType"\ **/>**                                       |
|                                                                       |
| **<xs:element** minOccurs="0" name="b" type="xs:string"\ **/>**       |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="aComplexType"\ **>**                        |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="a1s"                              |
| type="tns:a1ComplexType"\ **/>**                                      |
|                                                                       |
| **<xs:element** minOccurs="0" name="a2" type="xs:string"\ **/>**      |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="a1ComplexType"\ **>**                       |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** maxOccurs="unbounded" minOccurs="0" name="a1"         |
| nillable="true" type="xs:string"\ **/>**                              |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="MRequestResponse"\ **>**                    |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="return"                           |
| type="tns:mResponseType"\ **/>**                                      |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="mResponseType"\ **>**                       |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="c" type="xs:string"\ **/>**       |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:complexType** name="errorMessageFault"\ **>**                   |
|                                                                       |
| **<xs:sequence>**                                                     |
|                                                                       |
| **<xs:element** minOccurs="0" name="customFaultCode"                  |
| type="xs:string"\ **/>**                                              |
|                                                                       |
| **</xs:sequence>**                                                    |
|                                                                       |
| **</xs:complexType>**                                                 |
|                                                                       |
| **<xs:element** name="ErrorMessageFault" nillable="true"              |
| type="tns:errorMessageFault"\ **/>**                                  |
|                                                                       |
| **</xs:schema>**                                                      |
|                                                                       |
| **</wsdl:types>**                                                     |
|                                                                       |
| **<wsdl:message** name="MRequest"\ **>**                              |
|                                                                       |
| **<wsdl:part** element="tns:MRequest" name="parameters"\ **/>**       |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:message** name="MRequestResponse"\ **>**                      |
|                                                                       |
| **<wsdl:part** element="tns:MRequestResponse"                         |
| name="parameters"\ **/>**                                             |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:message** name="ErrorMessageException"\ **>**                 |
|                                                                       |
| **<wsdl:part** element="tns:ErrorMessageFault"                        |
| name="ErrorMessageException"\ **/>**                                  |
|                                                                       |
| **</wsdl:message>**                                                   |
|                                                                       |
| **<wsdl:portType** name="SOAPBlockingImpl"\ **>**                     |
|                                                                       |
| **<wsdl:operation** name="MRequest"\ **>**                            |
|                                                                       |
| **<wsdl:input** message="tns:MRequest" name="MRequest"\ **/>**        |
|                                                                       |
| **<wsdl:output** message="tns:MRequestResponse"                       |
| name="MRequestResponse"\ **/>**                                       |
|                                                                       |
| **<wsdl:fault** message="tns:ErrorMessageException"                   |
| name="ErrorMessageException"\ **/>**                                  |
|                                                                       |
| **</wsdl:operation>**                                                 |
|                                                                       |
| **</wsdl:portType>**                                                  |
|                                                                       |
| **<wsdl:binding** name="SOAPBlockingImplServiceSoapBinding"           |
| type="tns:SOAPBlockingImpl"\ **>**                                    |
|                                                                       |
| **<soap:binding** style="document"                                    |
| transport="http://schemas.xmlsoap.org/soap/http"\ **/>**              |
|                                                                       |
| **<wsdl:operation** name="MRequest"\ **>**                            |
|                                                                       |
| **<soap:operation** soapAction="" style="document"\ **/>**            |
|                                                                       |
| **<wsdl:input** name="MRequest"\ **>**                                |
|                                                                       |
| **<soap:body** use="literal"\ **/>**                                  |
|                                                                       |
| **</wsdl:input>**                                                     |
|                                                                       |
| **<wsdl:output** name="MRequestResponse"\ **>**                       |
|                                                                       |
| **<soap:body** use="literal"\ **/>**                                  |
|                                                                       |
| **</wsdl:output>**                                                    |
|                                                                       |
| **<wsdl:fault** name="ErrorMessageException"\ **>**                   |
|                                                                       |
| **<soap:fault** name="ErrorMessageException" use="literal"\ **/>**    |
|                                                                       |
| **</wsdl:fault>**                                                     |
|                                                                       |
| **</wsdl:operation>**                                                 |
|                                                                       |
| **</wsdl:binding>**                                                   |
|                                                                       |
| **<wsdl:service** name="SOAPBlockingImplService"\ **>**               |
|                                                                       |
| **<wsdl:port** binding="tns:SOAPBlockingImplServiceSoapBinding"       |
| name="SOAPBlockingImplPort"\ **>**                                    |
|                                                                       |
| **<soap:address**                                                     |
| location="https://api.ente.example/soap/nome-api/v1"\ **/>**          |
|                                                                       |
| **</wsdl:port>**                                                      |
|                                                                       |
| **</wsdl:service>**                                                   |
|                                                                       |
| **</wsdl:definitions>**                                               |
+-----------------------------------------------------------------------+

A seguire un esempio di chiamata al metodo **M**.

Endpoint

https://api.ente.example/soap/nome-api/v1

Method M

1. Request Body

+--------------------------------------------------------------+
| **<soap:Envelope**                                           |
|                                                              |
| xmlns:soap="http://www.w3.org/2003/05/soap-envelope"         |
|                                                              |
| xmlns:m="http://ente.example/nome-api" **>**                 |
|                                                              |
| **<soap:Header>**                                            |
|                                                              |
| *<!--Autenticazione-->*                                      |
|                                                              |
| **</soap:Header>**                                           |
|                                                              |
| **<soap:Body>**                                              |
|                                                              |
| **<m:MRequest>**                                             |
|                                                              |
| **<M>**                                                      |
|                                                              |
| **<oId>**\ 1234\ **</oId>**                                  |
|                                                              |
| **<a>**                                                      |
|                                                              |
| **<a1s><a1>**\ 1\ **</a1>**...\ **<a1>**\ 2\ **</a1></a1s>** |
|                                                              |
| **<a2>**\ RGFuJ3MgVG9vbHMgYXJlIGNvb2wh\ **</a2>**            |
|                                                              |
| **</a>**                                                     |
|                                                              |
| **<b>**\ Stringa di esempio\ **</b>**                        |
|                                                              |
| **</M>**                                                     |
|                                                              |
| **</m:MRequest>**                                            |
|                                                              |
| **</soap:Body>**                                             |
|                                                              |
| **</soap:Envelope>**                                         |
+--------------------------------------------------------------+

2. Response Body (HTTP status code 200 OK)

+------------------------------------------------------+
| **<soap:Envelope**                                   |
|                                                      |
| xmlns:soap="http://www.w3.org/2003/05/soap-envelope" |
|                                                      |
| xmlns:m="http://ente.example/nome-api" **>**         |
|                                                      |
| **<soap:Body>**                                      |
|                                                      |
| **<m:MRequestResponse>**                             |
|                                                      |
| **<return>**                                         |
|                                                      |
| **<m:c>**\ OK\ **</m:c>**                            |
|                                                      |
| **</return>**                                        |
|                                                      |
| **</m:MRequestResponse>**                            |
|                                                      |
| **</soap:Body>**                                     |
|                                                      |
| **</soap:Envelope>**                                 |
+------------------------------------------------------+

2. Response Body (HTTP status code 500 Internal Server Error)

+----------------------------------------------------------+
| **<soap:Envelope**                                       |
|                                                          |
| **xmlns:soap="http://www.w3.org/2003/05/soap-envelope"** |
|                                                          |
| **xmlns:m="http://ente.example/nome-api" >**             |
|                                                          |
| **<soap:Body>**                                          |
|                                                          |
| **<soap:Fault>**                                         |
|                                                          |
| **<soap:Code>**                                          |
|                                                          |
| **<soap:Value>soap:Receiver</soap:Value>**               |
|                                                          |
| **</soap:Code>**                                         |
|                                                          |
| **<soap:Reason>**                                        |
|                                                          |
| **<soap:Text xml:lang="en">Error</soap:Text>**           |
|                                                          |
| **</soap:Reason>**                                       |
|                                                          |
| **<soap:Detail>**                                        |
|                                                          |
| **<m:ErrorMessageFault>**                                |
|                                                          |
| **<customFaultCode>1234</customFaultCode>**              |
|                                                          |
| **</m:ErrorMessageFault>**                               |
|                                                          |
| **</soap:Detail>**                                       |
|                                                          |
| **</soap:Fault>**                                        |
|                                                          |
| **</soap:Body>**                                         |
|                                                          |
| **</soap:Envelope>**                                     |
+----------------------------------------------------------+
