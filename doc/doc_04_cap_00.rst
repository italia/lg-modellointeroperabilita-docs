Sicurezza del nuovo modello di interoperabilità


.. code-block:: XML

   <soap:Envelope>
     <soap:Header>
       <wsse:Security soap:mustUnderstand="1">
         <wsse:BinarySecurityToken 		EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary" 		ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" 
   wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7">MIICyzCCAbOgAwIBAgIECxY+9TAhkiG9w...
         </wsse:BinarySecurityToken>
         <wsu:Timestamp wsu:Id="TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">
           <wsu:Created>2018-10-04T10:17:28.061Z</wsu:Created>
           <wsu:Expires>2018-10-04T10:22:28.061Z</wsu:Expires>
         </wsu:Timestamp>
         <ds:Signature Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90">
           <ds:SignedInfo>
             <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
               <ec:InclusiveNamespaces PrefixList="soap" />
             </ds:CanonicalizationMethod>
             <ds:SignatureMethod 
                 Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
             <ds:Reference URI="#TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">
               <ds:Transforms>
                 <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                   <ec:InclusiveNamespaces PrefixList="soap wsse" />
                 </ds:Transform>
               </ds:Transforms>
               <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
               <ds:DigestValue>NWPKndUk42jwIJOpDGXACq7QbyBUg1UfJFSEylsCxQw=</ds:DigestValue>
             </ds:Reference>
           </ds:SignedInfo>
           <ds:SignatureValue>AIrDa7ukDfFJD867goC+c7K3UampxpX/Nj/...</ds:SignatureValue>
           <ds:KeyInfo Id="KI-cad9ee47-dec8-4340-8fa1-74805f7e26f8">
             <wsse:SecurityTokenReference wsu:Id="STR-e193f25f-9727-4197-b7aa-25b01c9f2ba3">
              <wsse:Reference 
                URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7"  ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>          </wsse:SecurityTokenReference>
           </ds:KeyInfo>
         </ds:Signature>
       </wsse:Security>
        </soap:Header>
     <soap:Body>
       <ns2:sayHi xmlns:ns2="http://example.profile.security.modi.agid.gov.it/">
         <arg0>Hello World!</arg0>
       </ns2:sayHi>
     </soap:Body>
   </soap:Envelope>     


.. toctree::
  :maxdepth: 3
  :caption: Indice dei contenuti

  introduzione.rst
  sicurezza-di-canale-eo-autenticazione-delle-organizzazioni.rst
  autenticazione-del-soggetto-richiedente.rst
  integrità.rst
  soluzioni-di-sicurezza.rst
  elenco-degli-algoritmi.rst
  bibliografia.rst
