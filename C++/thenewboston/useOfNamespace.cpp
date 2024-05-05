/* A namespace is a C++ feature that helps you organize and manage code by
 * providing a way to group related symbols (such as variables, functions, and
 * classes) under a common name. It's a way to avoid naming conflicts and
 * improve code modularity. */

namespace CompanyA {
void doSomething() {
  // Code for Company A's functionality
}
} // namespace CompanyA

namespace CompanyB {
void doSomething() {
  // Code for Company B's functionality
}
} // namespace CompanyB

int main() {
  CompanyA::doSomething(); // Calls Company A's function
  CompanyB::doSomething(); // Calls Company B's function

  return 0;
}

/* In this example, both CompanyA and CompanyB have their own doSomething
function, and using namespaces allows you to distinguish between them. Without
namespaces, calling doSomething could lead to confusion and conflicts.

Namespaces make your code more organized, easier to understand, and help prevent
unintended interactions between different parts of your program.*/
