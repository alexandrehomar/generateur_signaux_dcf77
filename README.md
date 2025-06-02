Dans ce projet, nous avons développé une application embarquée sur une carte STM32 utilisant le système d'exploitation temps réel FreeRTOS, dont l’objectif est de recevoir un message de 36 caractères via l’interface UART.
Pour cela, nous avons d’abord configuré l’UART en mode réception avec interruption, de façon à pouvoir capturer les données dès qu’elles arrivent sans bloquer le 
processeur. Une tâche FreeRTOS dédiée à la réception UART a ensuite été mise en place. Cette tâche récupère les messages reçus via une interruption (
grâce à HAL_UART_RxCpltCallback), puis les transmet à une file (queue) RTOS. En parallèle, une seconde tâche est responsable du décodage du message grâce à la fonction sscanf().
Elle lit les messages depuis cette file et les envoie à la fonction modulation, qui formate les informations pour la transmission selon la norme DCF 77.
Cette architecture en deux tâches indépendantes permet de garantir un fonctionnement fluide et réactif : la réception UART se fait de manière asynchrone, 
tandis que le formatage et la transmission est traitée de façon séquentielle sans perturber le reste du système. Ce découplage, rendu possible par l’utilisation des files FreeRTOS, 
assure une bonne séparation des responsabilités et facilite la maintenance du code.
![image](https://github.com/user-attachments/assets/52a344dd-9c18-4125-b4d8-b8c391cbfa51)
![image](https://github.com/user-attachments/assets/a55250e8-54db-43bd-b9e5-b0f71e7b21a7)


De même que le message, la transmission est normée : On transmet un bit par seconde, 0 -> 100ms en état bas, 1 -> 200ms en état bas
![image](https://github.com/user-attachments/assets/e75f20e1-62b8-464a-ba0c-3326e8d37569)
