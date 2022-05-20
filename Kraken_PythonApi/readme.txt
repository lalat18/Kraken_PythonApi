This is an Api client which will query to kraken public API and run some tests .
features:- 
  1. On this we have touched mostly all of the kraken public API endpoints 
  2. some of the Helper/Base modules are there which will be used across most of the standalone calls 
      a)new file:   Kraken_PythonApi/Source_Control/CodeRepositoary/QaUtility/Genericutilites.py
        Description : "This will generate the dynamic Payload everytime by querying to public api "
      b)new file:   Kraken_PythonApi/Source_Control/CodeRepositoary/QaUtility/Requestsutility.py
        Description : "This is the modified API client it will take parameters as endpot/payload and return result dictoonary "
  3. Some of the Config/Metadata that's used to retrive some of basic info across all the projects 
    a) Kraken_PythonApi/Source_Control/CodeRepositoary/Plugins/hosts_config.py 
        Meta data about the Base API URL and Environment(Default- Test)
    b)Kraken_PythonApi/Source_Control/CodeRepositoary/Plugins/InheritQafunction/package.json 
        Meta data of some returned API client calls , will be used to verify the response 
   4. Some of Package Modules which will be used to extract/process some of the logic , we made it generic so that it can be reused 
      a) Kraken_PythonApi/Source_Control/CodeRepositoary/Plugins/InheritQafunction/Qualitychecks_modules.py
      b) Kraken_PythonApi/Source_Control/CodeRepositoary/Plugins/InheritQafunction/Test_Trade_OHLC_cases.py
   5. All Test Cases are on one location , if we will run this folder then it will execute all the test cases
   
       a)  new file:   Kraken_PythonApi/Source_Control/Tests/test_DpthorderVerify.py
       b) new file:   Kraken_PythonApi/Source_Control/Tests/test_TcikerVerify.py
       c) new file:   Kraken_PythonApi/Source_Control/Tests/test_VerifyTrade.py
       d) new file:   Kraken_PythonApi/Source_Control/Tests/test_healthcheck.py
