#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *filePointer;
    char fileName[100];
    int choice;
    int numLines;

    // Get the filename from the user
    printf("Input the file name to be opened: ");
    scanf("%s", fileName);

    // Open the file in read/write mode
    filePointer = fopen(fileName, "r+");
    if (filePointer == NULL) {
        printf("File does not exist. Creating a new file.\n");
        filePointer = fopen(fileName, "w+");
    }

    if (filePointer == NULL) {
        printf("Failed to open the file.\n");
        return 1;
    }

    // Display a menu for adding, removing lines, or displaying the content
    printf("Menu:\n");
    printf("1. Add lines\n");
    printf("2. Remove lines\n");
    printf("3. Display content\n");
    printf("Enter your choice (1/2/3): ");
    scanf("%d", &choice);

    if (choice == 1) {
        // Get the number of lines to append from the user
        printf("Input the number of lines to be written: ");
        scanf("%d", &numLines);

        // Consume the remaining newline character left in the input buffer
        getchar();

        // Set the file pointer to the end of the file to append lines
        fseek(filePointer, 0, SEEK_END);

        // Write the new lines to the file
        printf("The lines are:\n");
        for (int i = 0; i < numLines; i++) {
            char newLine[1000];
            printf("Line %d: ", i + 1);
            fgets(newLine, sizeof(newLine), stdin);
            fputs(newLine, filePointer);
        }
    } else if (choice == 2) {
        // Read and display the current content of the file
        printf("Current content of the file %s is:\n", fileName);
        char line[1000];
        while (fgets(line, sizeof(line), filePointer) != NULL) {
            printf("%s", line);
        }

        // Create a temporary file to hold the modified content
        FILE *tempFilePointer;
        tempFilePointer = fopen("temp.txt", "w");

        if (tempFilePointer == NULL) {
            printf("Failed to create a temporary file.\n");
            return 1;
        }

        // Get the line number to remove from the user
        printf("Enter the line number to remove: ");
        scanf("%d", &numLines);

        // Reset the file pointer to the beginning of the file
        fseek(filePointer, 0, SEEK_SET);

        // Copy lines to the temporary file, excluding the specified line
        int currentLine = 1;
        while (fgets(line, sizeof(line), filePointer) != NULL) {
            if (currentLine != numLines) {
                fputs(line, tempFilePointer);
            }
            currentLine++;
        }

        // Close both files
        fclose(filePointer);
        fclose(tempFilePointer);

        // Remove the original file and rename the temporary file
        remove(fileName);
        rename("temp.txt", fileName);

        printf("Line %d has been removed.\n", numLines);
    } 
    else if (choice == 3) {
        // Display the content of the file
        printf("Content of the file %s is:\n", fileName);
        char line[1000];
        while (fgets(line, sizeof(line), filePointer) != NULL) {
            printf("%s", line);
        }
    } 
    else {
        printf("Invalid choice.\n");
    }

    // Close the file
    fclose(filePointer);

    return 0;
}