#include <iostream>
using namespace std;


void swap(int&, int&);
int partition(int[], int, int);
void quicksort(int[], int, int);

void merge(int arr[], int l, int m, int r);
void mergeSort(int arr[], int l, int r);

/* A utility function to swap two elements */
void swap(int& a, int& b)
{
	int tmp = a;
	a = b;
	b = tmp;
}

/* The main function that implements QuickSort
a[] --> Array to be sorted,
p   --> Starting index,
r   --> Ending index */
void quicksort(int a[], int p, int r)
{
	if (p < r)
	{
		int q = partition(a, p, r); // q is partitioning index, arr[q] is now at right place
		quicksort(a, p, q - 1);
		quicksort(a, q + 1, r);
	}
}


/* This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot */
int partition(int a[], int p, int r)
{
	int x = a[r];						// pivot
	int i = (p - 1);					// Index of smaller element
	for (int j = p; j <= r - 1; j++)
	{
		// If current element is smaller than or equal to pivot
		if (a[j] <= x)
		{
			i++;						// increment index of smaller element
			swap(a[i], a[j]);
		}
	}
	swap(a[i + 1], a[r]);
	return (i + 1);
}

/* Merges two subarrays of arr[]. First subarray is arr[l..m]. Second subarray is arr[m+1..r] */ 
void merge(int arr[], int l, int m, int r)
{
	const int n1 = m - l + 1;
	const int n2 = r - m;

	/* create temp arrays */
	int* L = new int[n1];
	int* R = new int[n2];

	/* Copy data to temp arrays L[] and R[] */
	for (int i = 0; i < n1; ++i)
		L[i] = arr[l + i];
	for (int j = 0; j < n2; ++j)
		R[j] = arr[m + 1 + j];

	/* Merge the temp arrays back into arr[l..r]*/
	int i = 0; // Initial index of first subarray 
	int j = 0; // Initial index of second subarray 
	int k = l; // Initial index of merged subarray 
	while (i < n1 && j < n2)
	{
		if (L[i] <= R[j])
		{
			arr[k] = L[i];
			i++;
		}
		else
		{
			arr[k] = R[j];
			j++;
		}
		k++;
	}

	// Copy the remaining elements of L[], if thereare any
	while (i < n1)
	{
		arr[k] = L[i];
		i++;
		k++;
	}

	// Copy the remaining elements of R[], if there are any */
	while (j < n2)
	{
		arr[k] = R[j];
		j++;
		k++;
	}
	delete[] L;
	delete[] R;
}

/* l is for left index and r is right index of the sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
	if (l < r)
	{
		// Same as (l+r)/2, but avoids overflow for large l and h 
		int m = l + (r - l) / 2;

		// Sort first and second halves 
		mergeSort(arr, l, m);
		mergeSort(arr, m + 1, r);

		merge(arr, l, m, r);
	}
}


int main()
{
	int a[] = { 5, 1, 9, 3, 8, 4, 1, 2, 6, 7 };
	int b[] = { 5, 1, 9, 3, 8, 4, 1, 2, 6, 7 };
	for (int i = 0; i < 10; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
	quicksort(a, 0, 9);
	for (int i = 0; i < 10; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
	
	mergeSort(b, 0, 9);
	for (int i = 0; i < 10; i++)
	{
		cout << b[i] << " ";
	}
	cout << endl;

	int kkk;
	cin >> kkk;
	return kkk;
}


