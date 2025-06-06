#include "DynamicIntArray.hpp"
        
DynamicIntArray::DynamicIntArray(const int capacity)
    : values(new int[capacity]), capacity(capacity), count(0) {}

DynamicIntArray::DynamicIntArray(const DynamicIntArray& other)
    : values(new int[other.capacity]), capacity(other.capacity), count(other.count) {
        for (int idx = 0; idx < count; ++idx)
            values[idx] = other.values[idx];
    }


DynamicIntArray::~DynamicIntArray() {
    delete [] values;
    values = nullptr;
    capacity = count = 0;
}

void DynamicIntArray::check_index(int& idx) const {
    if (idx < 0) idx += count;
    if (idx < 0 || idx >= count) 
        throw OutOfBoundsException();
}

int& DynamicIntArray::operator[](int idx) const {
    check_index(idx);
    return values[idx];
}

void DynamicIntArray::resize() {
    int *tmp = new int[capacity*2];
    for (int idx = 0; idx < capacity; ++idx)
        tmp[idx] = values[idx];
    delete [] values;
    values = tmp;
    capacity *= 2;
    std::cerr << "resized to " << capacity << ": "<< *this << std::endl;
}

void DynamicIntArray::append(int value) {
    if (count == capacity) resize();
    values[count++] = value;
}

void DynamicIntArray::shift_left(int idx) {
    for (int i = idx+1; i < count; ++i)
        values[i-1] = values[i];
    --count;
}

int DynamicIntArray::pop(int idx) {
    check_index(idx);
    int tmp = values[idx];
    shift_left(idx);
    return tmp;
}

int DynamicIntArray::size() const { return count; }
    
std::ostream& operator << (std::ostream& s, const DynamicIntArray& array) {
    s << "[";
    for (int idx = 0; idx < array.size(); ++idx) {
        if (idx != 0) s << ", ";
        s << array[idx];
    }
    s << "]";
    return s;
}
