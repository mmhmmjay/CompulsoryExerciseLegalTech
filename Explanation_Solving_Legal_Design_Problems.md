# CompulsoryExerciseLegalTech

Explanation: Solving Legal Design Problems 

 

Since both PCR-test-results and antibody-test results fall within different categories of data according to Art. 9 GDPR, I.e., health data and genetic data, I thought it would be reasonable, to divide both options into two different paths in the program. Although the same law applies, different derogations of art. 9 (2) GDPR can be more relevant and therefore, the order in which the possible exceptions are queried should differ to find an option for legal processing as fast as possible. Also, some derogations which do not appear to be relevant at all to the case at hand are not listed in the program. However, if people using the program are convinced, that another exception should apply, they are asked to contact their legal advisor. 

 

Then, I rewrote all the possibly applicable exceptions of Art. 9 (2) GDPR into individual yes-and-no-questions and attributed them all to different variables which describe the matter shortly. In real life, some of these questions would need further explanation and examples so laymen would be able to answer them correctly. 

 

When I started coding the program, I realised that writing out each possibility within the code itself would make it look messy and unclear. This is when I began writing functions for every possible exception according to Art. 9 (2) GDPR, which also can be reused for PCR- and antibody-test alike. This also has the advantage that the process of coding becomes clearer as well and other sorts of tests could be easily added to the program. 

 

Then I tried to solve the problem on how to “get back on track”: If at any point it becomes clear that the (or not all) conditions of an exception are not met and therefore, the conditions of the next possible exception need to be checked. Since I did not want to write out all possibilities step-by-step within the code, I used the possibility to attribute return values to the outcomes of my questions. Whenever the answer to a question is “no”, meaning not all of the conditions are met, I attribute the return “0”. If that happens at any point within the function, the program continues with the next function meaning tests for the next possible exception. 

 

Through all these measures, the code has become neat but still well-functioning. Also, it would be easy to add other derogations of Art. 9 (2) GDPR or to add other testing methods like antigen-tests. 
