# ML-LAT-NG-Analysis
ML Project to analysis diffrence between NG and OK parts from workshop based on their production DATA
<h1> Problem description </h1>
<p>Some pieces have been classified as not good on workshop. The classification results from the distribution of pressure over time. Pressure is checked in 3 points in time. The problem is to analyze the production data of ok and ng pieces and find the relationship that causes the pieces to be wrong. </p>

<p>At the beginning, the possibility of evaluating ok or ng on the basis of production data was checked. In the next step, an attempt was made to assess the pressure value in a given time unit based on all the collected results</p>

<img src="https://user-images.githubusercontent.com/109242797/218460467-c461cf73-3aaa-4208-b8e7-9c2dd5ea08c8.png" alt='not found' title='Gates_over_time'>

Main data file from workshop is constructed as:

<img src="https://user-images.githubusercontent.com/109242797/216564770-05948937-982a-4965-9ae3-ac226931b9fc.png" alt='not found' title='Main_Data_File'>

It contains:
<ol>
<li>Lot number - it is the set of pieces in which the piece was produced </li>
<li>Piece number - piece number which we analyse </li>
<li>Judgement - is it OK or NG on workshop</li>
</ol>
Additionaly there are 3 separated test temperatures (H - High, A - Ambient, L - Low). Each temperature has separated main data sheet.
<img src="https://user-images.githubusercontent.com/109242797/216568808-2330c1ce-d6ef-4eef-9ba3-1a8421691633.png" alt='not found' title='LAH Sheet'>

LOT File is constructed as follows:
<img src="https://user-images.githubusercontent.com/109242797/216568218-1b3cef63-2a3d-4797-a9f0-2448bb2d158f.png" alt='not found' title='LOT Data File'>
File name is a name of LOT in xlsx format.
Rows contains data for each produced piece. About 150 columns of data.
<br><br>
<h2> Steps: </h2> 
<ul>
<li>First point is to check OK/NG s/n from workshop and collect production data from separated files.</li>
<li>Second point is to analyze it using ML Methods.</li>
<li>Third point is to analyze it trying to predict pressure in each of 3 points of time using ML Methods.</li>
<li>Fourth point is to analyze it using DL Methods.</li>
</ul>

<h1> General OK/NG classification </h1>
This point collect all pieces (all temperatures and all gates) in one pool of data. An attempt to find a dependency without division into the test temperature and the time of occurrence of the incorrectness.
<h2> Data collection </h2>
Collect a production data for each piece from main data file using data_main.py from data.
Finally creates a new xlsx file with judgement from workshop and all production data columns generally pre-processed to avoid categorical data or data which is not crucial: <br></br>
<img src="https://user-images.githubusercontent.com/109242797/216572748-bad770f1-c6e6-4804-80ad-2d6ec53a9f0f.png" alt='not found' title='LOT Data File'>
<h2> General Schema for ML Methods: </h2>
<p>Each of the ML methods used is based on loading the necessary libraries, loading the data file created in the previous stage, scaling the data, finding the best parameters for the method using GridSearchCv, and finally creating a prediction model and estimating its effectiveness</p>
<h2> Logistic Regression </h2>
<h3>Finding best parameters by GridSearchCV gave results as follows:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218461534-1aa6ec05-fc18-482a-a21c-b694b08a8852.png" alt='not found' title='Parameters for LR'></p>

<h3>Confusion Matrix:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218461587-b38b8fbf-cb53-4710-abbc-94f9534467cc.png" alt='not found' title='CM for LR'></p>

<h3>Result </h3>
Logisticregression is a linear ML method. Using it in the above, non-linear example, as intended, does not bring any benefits. All of the samples were assigned to the OK group.

<h2> K-Nearest Neighbors </h2>
<h3>Finding best parameters by GridSearchCV gave results as follows:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218464154-c338be66-43bf-4fae-be9e-32186b43444f.png" alt='not found' title='Parameters for KNN'></p>

<h3>Confusion Matrix:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218464286-5de006bf-f5f9-45e9-99ff-733d075dfceb.png" alt='not found' title='CM for KNN'></p>

<h3>Result </h3>
The knn method gave slightly better results than the linear logisticregression. Some of the pieces were assigned to the NG group, but they were both ok and actually ng. Their distribution is 50/50 so it can be considered random. Anyway method find some reason to consider it as NG. Accuracy is also slightly better thank LR.

<h2> Support Vector Machine </h2>
<h3>Finding best parameters by GridSearchCV gave results as follows:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218465165-b069ab16-41d1-44b9-9175-71e01a152e73.png" alt='not found' title='Parameters for SVM'></p>

<h3>Confusion Matrix:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218465231-16102e3d-9bcd-4eae-91bf-d04a32e8bde7.png" alt='not found' title='CM for SVM'></p>

<h3>Result </h3>
Svm, by analogy with LogistiRegression, is a linear method that should not be used in the above case. Hence, the data is identical to that of LogisticRegression, i.e. all pieces have been assigned to the OK group.

<h2> Kernel SVM </h2>

<h3>Confusion Matrix:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218465771-5108b307-2b1d-4d24-b2fc-f45fb3e38649.png" alt='not found' title='CM for Kernel SVM'></p>

<h3>Result </h3>
In this case, a non-linear kernel for the svm method was used. this resulted in the correct classification of one piece as NG. Despite this, it is difficult for these methods to find a relationship that causes a wider division of elements as NG groups.

<h2> Naive Bayes </h2>
<h3>Finding best parameters by GridSearchCV gave results as follows:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218466875-7582ff5e-4767-42ba-a579-b5b8054b5d9d.png" alt='not found' title='Parameters for NB'></p>

<h3>Confusion Matrix:</h3>
<p><img src="https://user-images.githubusercontent.com/109242797/218466955-f0e3bc2d-3cf0-493a-994b-4363dd54f336.png" alt='not found' title='CM for NB'></p>


<h3>Result </h3>
Naive bayes assigned all pieces to the group ok


<h2> Decision Tree Classification </h2>
Decision tree is the first of the methods that found dependencies that match the pieces to the NG group. Therefore, a different approach was considered for this method. First, the confusion matrix and classification report for raw data were checked.
<p><img src="https://user-images.githubusercontent.com/109242797/218467895-4adf4da4-2bd2-4bba-b3c4-e5e4e92e81b9.png" alt='not found' title='DTRE'></p>
<p> The precision for the ok group increased compared to the previous methods, however, the recall significantly decreased. In the case of the ng group, the results are not correct </p>
<h3> Scaling </h3>
In the next step, an attempt was made to scale the data and check the effect on the results
<p><img src="https://user-images.githubusercontent.com/109242797/218468616-97e00e71-6e14-4dce-9458-e3c234d4efbc.png" alt='not found' title='DTRE'></p>
<p> There was no significant impact on the data in the case of rescaling the input data. </p>

<h3> Entropy </h3>
<p>In the final step, it was checked how changing the evaluation criteria for entropy would affect the results </p>
<p><img src="https://user-images.githubusercontent.com/109242797/218469037-9b94a15e-3d38-44ab-8c82-e338895407c3.png" alt='not found' title='DTRE'></p>
<p> Changing the criterion to entropy significantly improves the results. There has been an increase in precision for NG pieces, even though their recall has decreased. In the case of the OK group, the recall was increased while the accuracy of the assessment was maintained </p>

<h3> Graph </h3> 
<p>An extended graph with a maximum level of 10 has been generated. </p>
<p><img src="https://user-images.githubusercontent.com/109242797/218469602-908a0056-1599-478d-8ee9-4b71f7f148f3.png" alt='not found' title='GRAph'></p>

