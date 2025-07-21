<h1 align=center>Branch and Bound and Branch and Bound with subestimation</h1>

<p align="center">
  <img width="400px" src="https://github.com/AlejandroDavidArzolaSaavedra/practicas_fsi/assets/90756437/0156d764-228f-4ca3-b8df-716e36b95943"/>  
</p>

This practice has the objective of searching and comparing two heuristic searching methods commonly  used in
the resolution of searching problems in AI: "<strong>Branch and Bound</strong>" and "<strong>Branch and Bound with Subestimation Heuristic</strong>".

# 👥 Development team (Ctrl + Click to view profiles)

[![GitHub](https://img.shields.io/badge/GitHub-Andrea%20Santana%20Lopez-purple?style=flat-square&logo=github)](https://github.com/AndreaSantalos)

[![GitHub](https://img.shields.io/badge/GitHub-Alejandro%20David%20Arzola%20Saavedra-blue?style=flat-square&logo=github)](https://github.com/AlejandroDavidArzolaSaavedra)
  
## Summary
The principal purpose of this practice is to show how both methods generate the same optimal solution  when searching a route between diferent cities in
the graph of <strong>Romania's cities</strong>, as it is shown in the following image where we used networkx library.
<ul align="center">		
  <a href="https://en.wikipedia.org/wiki/Romania" target="_blank">
    <img style="width:30rem"  src="https://github.com/AlejandroDavidArzolaSaavedra/practicas_fsi/assets/90756437/abbc3b68-651c-4100-a7dc-0a4c81130e6e">
  </a>
</ul>

In this case,we have applied the algoritms Branch and Bound and Branch and Bound with Subestimation, <strong>the heuristic consists on  to
straight line since the state where we are until the final state</strong> where it's the optimal route between two cities in the graph of Romania's cities.

Althought both methods have the same result we can see that <strong>Branch and Bound with the heuristic applied expands less nodes in the searching graph</strong>.
What demonstrates its eficience regarding to computacionals resources.

We can see a comparation of the differences between the algoritms in the following  graphic where we can see the expanded nodes which are visited  by different algortims in different Romania's cities. For this, we used lightweight-charts.

## How you must execute the code
To execute the practice and to do testing ,follow this steps

1.You have to clonate this repository in your local machine:
```bash
git clone <https://github.com/AlejandroDavidArzolaSaavedra/practicas_fsi>
```
2. You have to search  the directory of the practice:
```bash
cd practicas_fsi
```
3. You must execute the principal program with the modified files:
```bash
python run.py
```
You have to see the results of the testings and the comparisons between the methods
# 🤝 Contributions

<img align="left" width="150" height="150" src="https://github.com/AlejandroDavidArzolaSaavedra/practicas_fsi/assets/90756437/53bfd2bf-273b-4d83-8041-382ee21aedec"></a>
<p width="200">If you wish to contribuite to this project you can do it.You can open "problems file"  or you can send pull requests to improve the code or adding new characteritics.</p>
