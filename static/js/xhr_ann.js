const postBtnANN = document.getElementById('ci-button-ann');

const sendHttpRequest = (method,url,data) => {
    const promise = new Promise((resolve,reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method,url);
        xhr.setRequestHeader('Content-Type','application/json');
        xhr.onload = () =>{
            if (xhr.status==200){
                resolve(JSON.parse(xhr.response))
            }
            else{
                reject(xhr.response)
            }
        }
        xhr.send(JSON.stringify(data));
    });
    return promise;
}

const sendDataANN = () => {
    sendHttpRequest('POST','http://localhost:8000/predict/api/heart_ann/',{
        age : document.querySelector("#age").value,
        sex : document.querySelector("#sex").value,
        cp : document.querySelector("#cp").value,
        trestbps : document.querySelector("#trestbps").value,
        chol : document.querySelector("#chol").value,
        fbs: document.querySelector("#fbs").value,
        restecg : document.querySelector("#restecg").value,
        thalach : document.querySelector("#thalach").value,
        exang : document.querySelector("#exang").value,
        oldpeak : document.querySelector("#oldpeak").value,
        slope : document.querySelector("#slope").value,
        ca : document.querySelector("#ca").value,
        thal : document.querySelector("#thal").value
    })
    .then(responseData => { 
        console.log(responseData);
        document.querySelector("#result_ann").innerHTML = responseData["result"]
        // document.getElementById("demo").innerHTML = text;
    })
    .catch(err =>{
        console.log(err);
    })
    ;
};

// const getData = () => {
//     sendHttpRequest('GET','http://localhost:8000/').then(responseData => {
//         console.log(responseData)
//         for(obj_data in responseData){
//             console.log(responseData[obj_data].id ,responseData[obj_data].Version_no)
//         }
//     })
    
// };

postBtnANN.addEventListener('click',sendDataANN)
// getBtn.addEventListener('click',getData)