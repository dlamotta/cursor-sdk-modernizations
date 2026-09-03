      *****************************************************************
      * INTCALC  -  savings interest for a statement period (legacy).
      * Known dust: DISPLAY debug, COMPUTE without ROUNDED, PIC that
      * truncates the daily rate so pennies disappear on small balances.
      *****************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. INTCALC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-PRINCIPAL         PIC 9(7)V99 VALUE 0012500.50.
       01  WS-ANNUAL-RATE       PIC 9V99 VALUE 0.05.
      * Rate was 5.25%; PIC 9V99 silently keeps 0.05.
       01  WS-DAYS              PIC 9(3) VALUE 031.
       01  WS-DAILY-RATE        PIC 9V9(4).
       01  WS-DAILY-INT         PIC 9(5)V99.
       01  WS-INTEREST          PIC 9(7)V99 VALUE ZERO.
       01  WS-NEW-BAL           PIC 9(7)V99.
       01  WS-I                 PIC 9(3).
       01  WS-SHOW              PIC $$,$$$,$$9.99.

       PROCEDURE DIVISION.
       MAIN-SECTION.
           DISPLAY "INTCALC START".
           DISPLAY "PRINCIPAL=" WS-PRINCIPAL.
           DISPLAY "RATE=" WS-ANNUAL-RATE.
           DISPLAY "DAYS=" WS-DAYS.
           PERFORM CALC-DAILY
           PERFORM ACCUMULATE
           PERFORM APPLY-TO-BAL
           DISPLAY "INTCALC END"
           STOP RUN.

       CALC-DAILY.
           COMPUTE WS-DAILY-RATE = WS-ANNUAL-RATE / 365.
           DISPLAY "DAILY RATE (TRUNC)=" WS-DAILY-RATE
           COMPUTE WS-DAILY-INT = WS-PRINCIPAL * WS-DAILY-RATE.
           DISPLAY "DAILY INT (TRUNC)=" WS-DAILY-INT.

       ACCUMULATE.
           MOVE ZERO TO WS-INTEREST
           PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > WS-DAYS
               ADD WS-DAILY-INT TO WS-INTEREST
               DISPLAY "DAY=" WS-I " RUNNING=" WS-INTEREST
           END-PERFORM.

       APPLY-TO-BAL.
           ADD WS-PRINCIPAL TO WS-INTEREST GIVING WS-NEW-BAL
           MOVE WS-NEW-BAL TO WS-SHOW
           DISPLAY "INTEREST=" WS-INTEREST
           DISPLAY "NEW BALANCE=" WS-SHOW.
