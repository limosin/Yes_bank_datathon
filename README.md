# Yes_bank_datathon
Recently I participated in the Yes Bank Campus Datathon. We were required to build a customer heatmap using the addresses given to us. Although the heat map construction was a relatively easier task after we get the geocoded latitudes and longitudes of the addresses, the main challenge here was data preprocessing. It required us to tag the specific cities from the addresses which were many a times not given in a proper format. There were also a large number of null values, which required us to predict the address using the other attributes available.


## Installtion Instructions
- Follow the instructions on this [page](https://github.com/uber/deck.gl/tree/master/examples/website/3d-heatmap) for deck.gl installations.
- Clone the repository in the master folder of 3D-Heatmap.
```bash
git clone https://github.com/limosin/Yes_bank_datathon
```
- Generate a subset of data using `data/dataset_gen,ipynb` to get the Mumbai data.
- Move to `src/` for the Data Preprocessing.
- See the preprocessed data in `data/Data_with_logits.csv`. You can find the generated latitudes and longitudes here.
- start the npm server using.
```bash 
npm start
```


## Output
![image](https://drive.google.com/uc?export=view&id=1-z8fnLlN4Vqp8fFA_bq0AbW2jqRbLVEI)
![image](https://drive.google.com/uc?export=view&id=1QcrFY1RlEGr8fmyyApFgjYkpyiY8sYgh)
![image](https://drive.google.com/uc?export=view&id=15YtzkIAkptxo80X6Bzxoju6cxm_rq-f0)
![image](https://drive.google.com/uc?export=view&id=1Wx5mmGlgAryMfjgCO_w4MofC59WhMG53)
