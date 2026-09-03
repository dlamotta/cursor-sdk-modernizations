      *****************************************************************
      * FEECALC  -  monthly maintenance fee on low-balance accounts.
      * Legacy quirks: fee table as REDEFINES, fee applied before
      * balance check completes, DISPLAY audit noise.
      *****************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FEECALC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-BALANCE           PIC 9(7)V99 VALUE 0000450.75.
       01  WS-MIN-BALANCE       PIC 9(5)V99 VALUE 500.00.
       01  WS-FEE               PIC 9(3)V99 VALUE 12.50.
       01  WS-NEW-BAL           PIC 9(7)V99.
       01  WS-FLAG              PIC X VALUE "N".
       01  WS-SHOW              PIC $$,$$$,$$9.99.

       PROCEDURE DIVISION.
       MAIN-SECTION.
           DISPLAY "FEECALC START".
           DISPLAY "BALANCE=" WS-BALANCE.
           DISPLAY "MIN=" WS-MIN-BALANCE.
           IF WS-BALANCE < WS-MIN-BALANCE
               MOVE "Y" TO WS-FLAG
               SUBTRACT WS-FEE FROM WS-BALANCE GIVING WS-NEW-BAL
               MOVE WS-NEW-BAL TO WS-SHOW
               DISPLAY "FEE APPLIED=" WS-FEE
               DISPLAY "NEW BALANCE=" WS-SHOW
           ELSE
               MOVE WS-BALANCE TO WS-NEW-BAL
               DISPLAY "NO FEE"
           END-IF
           DISPLAY "FEECALC END".
           STOP RUN.
