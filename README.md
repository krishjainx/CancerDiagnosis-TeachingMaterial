# Teaching Material for a HackClub workshop 
<h2>Krish </h2>


Objective: Make an AI figure out whether a tumor is malignant or benign. You can learn more about this [here](https://www.cancercenter.com/community/blog/2017/12/whats-the-difference-benign-and-malignant-tumors). Some more in depth resources to understand this if you are interested is:
1. https://www.nhs.uk/conditions/malignant-brain-tumour/
2. https://jamanetwork.com/journals/jamaoncology/fullarticle/2768634
3. https://www.nhs.uk/conditions/benign-brain-tumour/
4. https://www.nhsinform.scot/illnesses-and-conditions/cancer/cancer-types-in-adults/malignant-brain-tumour-cancerous
5. https://www.cancer.gov/about-cancer/understanding/what-is-cancer

What is this GitHub repository for?
- Good for teaching you the basics of using TensorFlow and neural networks
- Not ideal for using the code as is - must be modified to use in actual application

Why this is important?
- About 1 in 8 women (US) will be diagnosed with breast cancer - https://www.breastcancer.org/symptoms/understand_bc/statistics
- Correct cancer diagnosis is important for an "appropriate and effective treatment", as was also claimed by the WHO
- Some kinds of cancer are misdiagnosed at rates as high as 61 percent, according to the American Cancer Society (https://www.cancer.org/)
- Estimates demonstrate that ~ 20% of all cases of cancer are misdiagnosed (so ~ 80% will get the right treatment and diagnosis on first visit). Some will be sent back home with wrong treatment or diagnosis
-  Thus, women or men diagnosed with breast cancer often consult a second oncologist to ensure treatment/diagnosis is correct (costs money, long wait). Get second consultation from ML (can be trained as well as doctor, is faster than a doctor's diagnosis, not expensive)  


Key Stuff
- Malignant (Tumor that must be removed)
- Benign (Tumor that is not cancerous)
- Supervised ML - We know whether tumor is malignant or benign (labeled data)
- Cleaned data - Clean it of not needed useless/relevant info for this task of tumor classification
- 80% training data, 20% test data


Install dependencies:

```
pip3 install pandas sklearn tensorflow keras 
````


- Dataset from tumors coming from Wisconson's breast cancer dataset (which is a simplified clean version of the dataset here: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
 1. Diagnosis 
 - 1 - Malignant
 - 2 - Benign
 2. Numerical values relating to tumors that may or may not be cancerous - measurements describe properties of the cell's nucleus (eg, perimetr, texture, area, size )

References for datasets, TensorFlow docs and papers on cancer survival to shed light into how important proper diagnosis is
- https://www.kaggle.com/amandam1/breastcancerdataset
- https://www.jmir.org/2019/7/e14464/
- https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-019-4121-7
- https://data.gov.uk/
- https://www.kaggle.com/raghadalharbi/breast-cancer-gene-expression-profiles-metabric
- https://www.tensorflow.org/api_docs/python/tf/all_symbols
- https://www.nhs.uk/
- https://www.nationalbreastcancer.org/breast-tumors/
- https://www.sciencedirect.com/science/article/pii/S0923753419569770



________________________________________________________________________________________________________________________________________________________________
**
DISCLAIMER: I am not a medical professional**
