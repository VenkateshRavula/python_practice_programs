data_to_update = {'certificateDetails':[{'aiasName': 'Updated vcenter'}]}

data = {
   "type":"CertificateInfoV2",
   "certificateDetails":[
      {
         "type":"CertificateDetailV2",
         "base64Data":"test",
         "signatureAlgorithm":"SHA256WITHRSA",
         "issuer":"172.18.13.11",
         "aliasName":"",
         "commonName":"172.18.13.11",
         "alternativeName":"172.18.13.11",
         "name":"",
         "crlDistributionEndPoints":[

         ],
         "uri":""
      }
   ],
   "certificateStatus":{
      "chainStatus":"VALID",
      "selfsigned":"true",
      "trusted":"false"
   },
   "name":"",
   "description":"",
   "created":"2020-04-08T05:33:21.599Z",
   "modified":"2020-04-08T05:33:21.599Z",
   "eTag":"2020-04-08T05:33:21.599Z",
   "category":"appliance",
   "uri":"/rest/certificates/https/remote/172.18.13.11:443",
   "state":"Untrusted",
   "status":"OK"
}

data.update(data_to_update)
print(data)