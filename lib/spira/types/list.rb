module Spira::Types

  ##
  # A {Spira::Type} for arrays. They will be serialized to `RDF::List`s.
  #
  # @see Spira::Type
  # @see http://rdf.rubyforge.org/RDF/Literal.html
  class List
    include Spira::Type

    def self.unserialize(value)
      return [value.object] unless value.is_a? RDF::List
      ary = []
      rest = value.dup
      until rest.nil?
        if rest.first.is_a? RDF::List
          ary << self.unserialize(rest.first)
        else
          ary << rest.first.object
        end
        rest = rest.rest
      end
      ary
    end

    def self.serialize(value)
      RDF::List.send(:[], *value)
    end

    register_alias RDF::List
  end
end
