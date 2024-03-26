---

# Testosterone-Deficiency-ML-App

This project aims to develop machine learning models to test for Testosterone Deficiency in patients. The dataset used contains information on 3397 patients considered for Testosterone Deficiency. The dataset has been ethically approved by the Research Ethics Committee of the State University of Feira de Santana, Bahia, Brazil, under approval code: 3,057,301.


## Roadmap

- Created a colab notebook where I performed EDA and experimented with various parameters to successfully create 5 ML models.
- Then, created a local environment for VS Code.
- Created a `main.py` file to build a Streamlit file as the **frontend**.
- Simultaneously, created utils files `get_data.py`, `get_model.py`, `get_prediction.py` as the **backend** to process data, load pre-trained models from `.pkl` and `.pth` files, and then created `outputs` file to generate predictions.
- Now, built a Docker image using a **Dockerfile** to store in `Azure Container Registry` so that we could deploy this ML app using Docker.



## Evaluation Metrics

| Model | Accuracy | Precision | Specificity | Sensitivity | F1 Score | ROC AUC |
|-------|----------|-----------|-------------|-------------|----------|---------|
| SVM   | 88.62    | 92.70     | 92.70       | 82.33       | 87.20    | 0.8827  |
| RF    | 85.88    | 84.25     | 84.25       | 86.13       | 85.18    | 0.8589  |
| XGB   | 86.20    | 87.26     | 87.26       | 82.77       | 84.96    | 0.8601  |
| KNN   | 80.72    | 73.08     | 73.08       | 93.51       | 82.04    | 0.8142  |
| ANN   | 81.05    | 76.17     | 76.17       | 87.05       | 81.25    | 0.8138  |

---

## Models Developed
- Support Vector Machine (SVM)
- Random Forest (RF)
- XGBoost (XGB)
- k-Nearest Neighbors (KNN)
- Artificial Neural Network (ANN)
## Screenshots

[![MLApp1.png](https://i.postimg.cc/d1ZfqyZR/MLApp1.png)](https://postimg.cc/PphyyN4N)

[![MLApp2.png](https://i.postimg.cc/BQpmfgw9/MLApp2.png)](https://postimg.cc/PPLWmmj2)

[![MLApp3.png](https://i.postimg.cc/8PXLbn05/MLApp3.png)](https://postimg.cc/w7JtqFH8)
## Preferred IDE: VSCode

### Test the streamlit app on local:

1. Install required dependencies on local:

```commandline
pip install -r requirements.txt
```


2. Test the streamlit app on local:

```
streamlit run main.py
```


### Building the docker image

(Note: Run as administrator on Windows and remove "sudo" in commands)

3. Important - Make sure you have installed Docker on your PC:
- Linux: Docker
- Windows/Mac: Docker Desktop

4. Start Docker:
- Linux (Home Directory):
  ```
  sudo systemctl start docker
  ```
- Windows: You can start Docker engine from Docker Desktop.

5. Build Docker image from the project directory:

```commandline
sudo docker build -t Image_name:tag .
```

### (Note: Rerun the Docker build command if you want to make any changes to the code files and redeploy.)

### Running the container & removing it

6. Switch to Home Directory:

```
cd ~
```
### (Note: cd / in windows)

List the built Docker images
```
$ sudo docker images
```

7. Start a container:
```commandline
sudo docker run -p 8501:8501 Image_ID
```

8. This will display the URL to access the Streamlit app (http://0.0.0.0:8501). Note that this URL may not work on Windows. For Windows, go to http://localhost:8501.

9. In a different terminal window, you can check the running containers with:
```
sudo docker ps
```

10. Stop the container:
 - Use `ctrl + c` or stop it from Docker Desktop.

11. Check all containers:
 ```
 sudo docker ps -a
 ```

12. Delete the container if you are not going to run this again:
 ```
 sudo docker container prune
 ```

### Pushing the docker image to Docker Hub

13. Sign up on Docker Hub.

14. Create a repository on Docker Hub.

15. Log in to Docker Hub from the terminal. You can log in with your password or access token.
```
sudo docker login
```

17. Tag your local Docker image to the Docker Hub repository:
 ```
 sudo docker tag Image_ID username/repo-name:tag
 ```

17. Push the local Docker image to the Docker Hub repository:
 ```
 sudo docker push username/repo-name:tag
 ```

(If you want to delete the image, you can delete the repository in Docker Hub and force delete it locally.)

18. Command to force delete an image (but don't do this yet):
 ```
 $ sudo docker rmi -f IMAGE_ID
 ```
## Authors

- Anmol Chhetri



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://linktr.ee/AnmolChhetri2000)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anmol1512/)


## Acknowledgements

 - I express my gratitude to UroS, the research group in Urology and Population Subgroups, from the Medical School, Universidade Estadual de Feira de Santana, for providing this valuable dataset.

