; 
            icl 'chall.inc'
;
; Start of code
;
            org $5000
;
            eor XMTDON
            .byte $9B
L5003       ldx #$20
            lda #$03
            sta IOCB0+ICCOM,X
            lda #$00
            sta IOCB0+ICBAL,X
            lda #$50
            sta IOCB0+ICBAH,X
            lda #$0B
            sta IOCB0+ICAX1,X
            lda #$00
            sta IOCB0+ICAX2,X
            jsr CIOV
            lda #$0B
            sta IOCB0+ICCOM,X
            lda #$9A
            sta IOCB0+ICBAL,X
            lda #$50
            sta IOCB0+ICBAH,X
            rts
L5031       ldx #$20
            lda #$28
            sta IOCB0+ICBLL,X
            lda #$00
            sta IOCB0+ICBLH,X
            jsr CIOV
            rts
L5041       ldx #$20
            lda #$0C
            sta IOCB0+ICCOM,X
            jsr CIOV
            rts
L504C       ldx #$20
            lda #$03
            sta IOCB0+ICCOM,X
            lda #$04
            sta IOCB0+ICAX1,X
            jsr CIOV
            lda #$07
            sta IOCB0+ICCOM,X
L5060       lda #$C2
L5062       sta IOCB0+ICBAL,X
            lda #$50
L5067       sta IOCB0+ICBAH,X
            rts
L506B       ldx #$20
            lda #$1A
            sta IOCB0+ICBLL,X
            lda #$00
            sta IOCB0+ICBLH,X
            jsr CIOV
            rts
L507B       ldx #$20
            lda #$03
            sta IOCB0+ICCOM,X
            lda #$0B
            sta IOCB0+ICAX1,X
            jsr CIOV
            lda #$0B
            sta IOCB0+ICCOM,X
            lda #$9A
            sta IOCB0+ICBAL,X
            lda #$50
            sta IOCB0+ICBAH,X
            rts
L509A       .byte $0C
            lda #$50
            sta DOSINI+1
            jmp L50A5
            jsr L50B0
L50A5       lda #$00
            sta MEMLO
            lda #$59
            sta MEMLO+1
            rts
L50B0       jmp (L5062)
            lda #$3F
            sta L5067+1
            lda L5060+1
            asl
            tay
            jsr L50C1
            rts
L50C1       .byte $B9,$D9
;
            org $5200
;
L5200       .byte $14
            asl LE00C,X
            bmi L5262
            dec L36F0
            ldx L39FC
            .byte $1A
            sta (L00CE),Y
            ldy L00C4,X
            asl LF318
            iny
            stx L850A
            inc L00BD,X
L521A       .byte $43
            ora (LTEMP+1),Y
            .byte $F2
            adc #$AB
            bit L1399
            .byte $12
            cmp (COUNTR),Y
            txs
            .byte $8F
            asl L3792
            .byte $F4
            tax
            eor IOCB3+ICPTH
            .byte $89
            dex
            .byte $FF,$1A
L5234       eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
            eor (SOUNDR,X)
L524E       .byte $7F,$47,$4F,$4F,$44
            jsr L4F4A
            .byte $42
            and (ICHIDZ,X)
            eor DRKMSK
            lsr
            .byte $4F
            eor L5420,Y
            pha
            .byte $4F
L5262       .byte $53
            eor ICHIDZ
            .byte $52
            eor COLCRS+1
            eor LMARGN
            .byte $53
            eor #$4E
            .byte $47
            jsr L5453
            .byte $4F
            lsr L5A4B
L5275       and (COUNTR+1,X)
            lsr L4349
            eor ICHIDZ
            .byte $54,$52
            eor L202C,Y
            eor L5941
            .byte $42
            eor ICHIDZ
            lsr L5845
            .byte $54
            jsr L4954
            eor L2045
            eor #$54
            .byte $53
            jsr L4F43
            .byte $52,$52
            eor FMSZPG
            .byte $54,$3A
            plp
L529E       ldx #$00                 #X=0
L52A0       lda #$01		     #acc=1
            stx L0000		     #L0000= X(=0)
            and L0000		     #L000(X) & acc
            beq L52BC		     #if ==0 goto  L52BC
            lda L50C1+1,X	     #acc= 50C2[X]
            dex			     #X-=1
            eor L521A,X		     #acc= 521A[X] ^ acc (521A[X-1] ^ 50C2[X])
            inx			     #X+=1
            sta L5234,X		     #5324[X] =acc
            cld
            rol L5234,X		     #ROL (5234[X])
            bcs L52E2
            jmp L52DC		     #jmp L52DC

L52BC       lda L50C1+1,X	     #acc= 50C2[X]
            inx			     #X+=1
            eor L50C1+1,X	     #acc= 50C2[X+1] ^ acc( 50C2[X+1] ^ 50C2[X])
            dex			     #X-=1
            sta L5234,X		     #5234[X] = acc
            lda L0000		     #acc= L0000 (=0)
            adc L50C1+1,X
            tay
            lda L5234,X
            sta L5234,X
            cld
            rol L5234,X		     #ROL(5234[X])
            bcs L52E2
            jmp L52DC		     #jmp L52DC

L52DC       inx     		     #X+=1
            cpx #$1A		     #compare X with 0x1A
            bne L52A0		     #if not equal j 52A0  
            rts

L52E2       inc L5234,X              #acc =5234[X]+1
            jmp L52DC

L52E8       ldx #$00 		     #X= 0x0

L52EA       lda L5200,X		     #acc =5200[X]
            cmp L5234,X              #compare acc with 5234[X]
            bne L52FA		     #if not equal -->fail
            inx			     #X+=1
            cpx #$1A		     # compare X with 0x1A
            bne L52EA		     
            jmp L530D		     #jmp L530D

L52FA       jsr L531D
            ldx #$00

L52FF       lda L5275+1,X
            sta L509A,X
            inx
            cpx #$28
            bne L52FF
            jmp L531A
	
L530D       ldx #$00			#X=0

L530F       lda L524E,X			#acc =524E[X]    -->Good Job
            sta L509A,X			#509A[X] =acc
            inx			        #X+=1
            cpx #$28			#compare X with 0x28
            bne L530F

L531A       lda #$00
            rts

L531D       ldx #$28
L531F       dex
            sta L509A,X
            bne L531F
            rts
            .byte $53
;
            org $0600
;
L0600       .byte $47
            eor #$4D
            eor L2045
            lsr DSTAT
            eor (FMSZPG+4,X)
            jsr L4E41
            .byte $44
            jsr L4547
            .byte $54
            jsr L5453
            .byte $4F
            lsr L534B
            rol L4620,X
            asl L00A2
            .byte $00
L061F       lda L0600,X
            sta L509A,X
            inx
            cpx #$1A
            bne L061F
            jsr L5003
            jsr L5031
            jsr L504C
            jsr L506B
            jsr L529E
            jsr L52E8
            jsr L507B
            jsr L5031
            jsr L5041
            rts
            lda #$3E
            ldx #$28
L064A       dex
            sta L509A,X
            bne L064A
            rts
            .byte $00
;
         
