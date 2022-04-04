// 050422

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getRandNum();
char* getRandWord();
int getUserGuess();
int userWon();
int userLost();

int main()
{
    printf("Hello, let's play hangman!\nThe category will be fruits!\nI'm thinking of a word.. and done!\n\n");

    int randNum = getRandNum();
    //printf("%d\n", randNum);
    char randWord[20];
    strcpy(randWord, getRandWord(randNum));
    //printf("%s\n", randWord);

    for (int a=0;a<strlen(randWord);a++){randWord[a] = toupper(randWord[a]);}
    //printf("%s\n", randWord);
    for (int a=0;a<strlen(randWord);a++){printf("-");}printf("\n");

    /*
    char space[20];
    for (int a=0;a<strlen(randWord);a++){strcat(space, "-");}
    printf(("%s\n", space));
    // this way of writing seems to draw some weird characters
    */

    // create boolean values for each char in randWord
    int ans[strlen(randWord)];
    for (int i=0;i<strlen(randWord);i++)
    {
        ans[i] = 0;
    }

    int lives = 10;
    while (lives)
    {

        char userGuess = getUserGuess();

        // check if user guess is correct
        int inWord = 0;
        for (int k=0; k<strlen(randWord); k++)
        {
            if (userGuess == randWord[k])
            {
                ans[k] = 1;
                inWord = 1;
            }
        }
        if (!inWord)
        {
            printf("No, %c is not in the word.\n", userGuess);
            lives--;
        }
        else
        {
            printf("Yes, %c is in the word!\n", userGuess);
        }

        //print spaces/guessed chars
        for (int j=0;j<strlen(randWord);j++)
        {
            if (ans[j] == 1)
            {
                printf("%c", randWord[j]);
            }
            else
            {
                printf("-");
            }
        }
        printf("\n");

        //check if player has won
        int counter = 0;
        for (int l=0;l<strlen(randWord);l++)
        {
            if (ans[l])
            {
                counter++;
            }
        }
        if (counter == strlen(randWord))
        {
            userWon(lives);
        }
        printf("You have %d lives left\n\n", lives);
    }
    userLost();
    return 0;
}


int getRandNum()
{
    srand(time(0));
    int randNum = rand()%8;  // number between 0-7
    return randNum;
}


char* getRandWord(num)
{
    char *WORDLIST[] = {"APPLE", "ORANGE", "DURAIN", "JACKFRUIT", "MANGO", "PEACH", "KIWI", "LYCHEE"};
    return WORDLIST[num];
}


int getUserGuess()
{
    char ug;
    printf("Your guess: ");
    scanf(" %c", &ug);
    ug = toupper(ug);
    return ug;
}


int userWon(livesLeft)
{
    printf("\nYou won with %d lives left!\n", livesLeft);
    exit(0);
}


int userLost()
{
    printf("\nYou ran out of lives!\nYou lost!\n");
    exit(0);
}
