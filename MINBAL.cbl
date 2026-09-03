      *****************************************************************
      * MINBAL   -  reject withdrawals that breach minimum balance.
      * Legacy quirks: compares PIC sizes that truncate cents, status
      * code buried in a REDEFINES block.
      *****************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MINBAL.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-BALANCE           PIC 9(7)V99 VALUE 0001200.00.
       01  WS-WITHDRAW          PIC 9(7)V99 VALUE 0000950.00.
       01  WS-MIN-REMAIN        PIC 9(5)V99 VALUE 500.00.
       01  WS-REMAIN            PIC 9(7)V99.
       01  WS-STATUS.
           05 WS-STATUS-CODE    PIC 9 VALUE 0.
           05 WS-STATUS-TEXT    PIC X(20) VALUE SPACES.

       PROCEDURE DIVISION.
       MAIN-SECTION.
           DISPLAY "MINBAL START".
           DISPLAY "BALANCE=" WS-BALANCE.
           DISPLAY "WITHDRAW=" WS-WITHDRAW.
           SUBTRACT WS-WITHDRAW FROM WS-BALANCE GIVING WS-REMAIN.
           DISPLAY "REMAIN=" WS-REMAIN.
           IF WS-REMAIN < WS-MIN-REMAIN
               MOVE 9 TO WS-STATUS-CODE
               MOVE "BELOW MINIMUM" TO WS-STATUS-TEXT
               DISPLAY "REJECTED=" WS-STATUS-TEXT
           ELSE
               MOVE 0 TO WS-STATUS-CODE
               MOVE "OK" TO WS-STATUS-TEXT
               DISPLAY "APPROVED=" WS-STATUS-TEXT
           END-IF
           DISPLAY "MINBAL END".
           STOP RUN.
